from datetime import datetime


def parse_datetime(dt: str) -> datetime:
    formats = ["%Y-%m-%d %H:%M:%S%z", "%Y-%m-%d %H:%M"]
    for fmt in formats:
        try:
            return datetime.strptime(dt, fmt)
        except ValueError:
            pass
    raise ValueError(f"Error! Failed to parse provided datetime format: {dt}")
