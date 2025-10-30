import datetime
from datetime import timedelta
from zoneinfo import ZoneInfo

class AuditTrail:
    def __init__(self, trail: list[str]):
        self.timeStamp = datetime.datetime.fromisoformat(trail[0])
        self.correctDuration = timedelta(minutes=int(trail[1]))
        self.wrongDuration = timedelta(minutes=int(trail[2]))

    def __repr__(self):
        return f"{__class__.__name__} {self.timeStamp} {self.correctDuration} {self.wrongDuration}"

    def correct(self):
        print(
            self.timeStamp.__str__() == self.timeStamp.astimezone(ZoneInfo("America/Halifax")).__str__(),
            self.timeStamp.__str__() == self.timeStamp.astimezone(ZoneInfo("America/Santiago")).__str__()
        )
        return self.timeStamp - (self.wrongDuration + self.correctDuration)

with open("resources/Puzzle7.txt") as puzzle_input_file:
    for split in [line.strip().split("\t") for line in puzzle_input_file]:
        d = AuditTrail(split).correct()
        # print(d,
        #   d.astimezone(ZoneInfo("America/Halifax")),
        #   d.astimezone(ZoneInfo("America/Halifax")).dst(),
        #   d.astimezone(ZoneInfo("America/Santiago")),
        #   d.astimezone(ZoneInfo("America/Santiago")).dst()
        # )




# for d in [datetime.datetime.fromisoformat(d) for d in ["2012-11-05T09:39:00.000-04:00", "2012-05-27T17:38:00.000-04:00", "2008-03-23T05:02:00.000-03:00"]]:
#     print(d,
#           d.astimezone(ZoneInfo("America/Halifax")),
#           d.astimezone(ZoneInfo("America/Halifax")).dst(),
#           d.astimezone(ZoneInfo("America/Santiago")),
#           d.astimezone(ZoneInfo("America/Santiago")).dst()
#           )

