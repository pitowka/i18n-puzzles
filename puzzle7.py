import datetime
from datetime import timedelta
from zoneinfo import *

from more_itertools.more import first


class AuditTrail:
    def __init__(self, trail: list[str]):
        self.timeStamp = datetime.datetime.fromisoformat(trail[0])
        self.correctDuration = timedelta(minutes=int(trail[1]))
        self.wrongDuration = timedelta(minutes=int(trail[2]))

    def correct(self):
        tz_info = next(ts.tzinfo for ts in
                  [self.timeStamp.astimezone(ZoneInfo("America/Halifax")), self.timeStamp.astimezone(ZoneInfo("America/Santiago"))]
                  if ts.__str__() == self.timeStamp.__str__())

        return (self.timeStamp - self.wrongDuration + self.correctDuration).astimezone(tz_info)


with open("resources/Puzzle7.txt") as puzzle_input_file:
    hours = enumerate(
        AuditTrail(split).correct().hour for split in
        [line.strip().split("\t") for line in puzzle_input_file])

    print(sum((e[0] + 1) * e[1] for e in hours))

