

from datetime import datetime, timezone


def current_date_utc() -> datetime:
    return datetime.now(tz=timezone.utc)

def timestamp_to_date(value: int) -> datetime:
    return datetime.fromtimestamp(value, tz=timezone.utc)

def date_to_timestamp(value: datetime) -> int:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("Datetime must be timezone-aware")
    
    return int(value.timestamp())