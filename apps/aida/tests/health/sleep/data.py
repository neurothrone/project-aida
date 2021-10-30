from collections import namedtuple

SleepData = namedtuple("SleepData", "slept_at awoke_at")
SleepField = namedtuple("SleepField", "attribute expected_label")

SLEEP_DATA = [
    SleepData(slept_at="2021-10-25 02:30:00+00:00", awoke_at="2021-10-25 12:00:00+00:00"),
    SleepData(slept_at="2021-10-26 08:00:00+00:00", awoke_at="2021-10-26 16:00:00+00:00"),
    SleepData(slept_at="2021-10-27 08:00:00+00:00", awoke_at="2021-10-27 16:50:00+00:00")
]
TEST_SLEEP_FIELDS = [
    SleepField("slept_at", "slept at"),
    SleepField("awoke_at", "awoke at"),
    SleepField("duration", "duration"),
]
