

from datetime import datetime, timezone


def current_date_utc() -> datetime:
    return datetime.now(tz=timezone.utc)

def timestamp_to_date(value: int) -> datetime:
    return datetime.fromtimestamp(value, tz=timezone.utc)

def date_to_timestamp(value: datetime) -> int:
    return int(value.timestamp())