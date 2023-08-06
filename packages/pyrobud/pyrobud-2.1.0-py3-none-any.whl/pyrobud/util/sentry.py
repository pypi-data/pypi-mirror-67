import logging
import sqlite3
import traceback
from pathlib import Path
from typing import Any, Dict, Optional, Type

import plyvel

import ratelimit
import sentry_sdk
import telethon as tg

from .. import __version__
from . import error, git, version

Event = Dict[str, Any]
EventHint = Dict[str, Any]

PUBLIC_CLIENT_KEY = (
    "https://75fe67fda0594284b2c3aea6b90a1ba7@o120089.ingest.sentry.io/1817585"
)

log = logging.getLogger("sentry")


# Dummy function for ratelimiting: 3 events/min
@ratelimit.limits(calls=3, period=60)
def _ratelimit() -> None:
    pass


def _send_filter(event: Event, hint: EventHint) -> Optional[Event]:
    try:
        # Discard event if ratelimit is exceeded
        try:
            _ratelimit()
        except ratelimit.RateLimitException:
            return None

        if "exc_info" in hint:
            exc_type: Type[BaseException]
            exc_value: BaseException
            exc_type, exc_value = hint["exc_info"][:2]

            # User-initiated interrupts, network errors, and I/O errors
            if exc_type in (
                KeyboardInterrupt,
                ConnectionError,
                IOError,
                sqlite3.OperationalError,
                plyvel.IOError,
                tg.errors.FloodWaitError,
                tg.errors.PhoneNumberInvalidError,
            ):
                return None

            exc_msg = str(exc_value)

            # Pillow error for invalid user-submitted images
            if exc_msg.startswith("cannot identify image file"):
                return None

            # Telegram connection errors
            if (
                exc_msg.startswith("Automatic reconnection failed")
                or exc_msg.startswith("Request was unsuccessful")
                or "Connection to Telegram failed" in exc_msg
                or "consecutive sign-in attempts failed" in exc_msg
            ):
                return None

            # Check involved files
            if getattr(exc_value, "__traceback__", None):
                tb = traceback.extract_tb(exc_value.__traceback__)
                for frame in tb:
                    # Ignore custom module errors
                    if Path(frame.filename).parent.stem == "custom_modules":
                        return None

        return event
    except Exception as e:
        log.error("Error running event filter", exc_info=e)

        # Inject error and return
        if "extra" not in event:
            event["extra"] = {}
        event["extra"]["send_filter_error"] = error.format_exception(e)
        return event


def init() -> None:
    """Initializes automatic Sentry error reporting."""

    # Use Git commit if possible, otherwise fall back to the version number
    release = version.get_commit()
    if release is None:
        release = __version__

    # Skip Sentry initialization if official status has been lost
    if not git.is_official():
        log.warning("Skipping Sentry initialization due to unofficial status")
        return

    # Initialize the Sentry SDK using the public client key
    sentry_sdk.init(PUBLIC_CLIENT_KEY, release=release, before_send=_send_filter)
