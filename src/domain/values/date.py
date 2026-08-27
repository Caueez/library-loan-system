

from datetime import datetime, timezone


def current_date_utc() -> datetime:
    return datetime.now(tz=timezone.utc)