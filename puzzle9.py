from collections import defaultdict
from datetime import datetime


class DairyEntry:
    def __init__(self, entry: str):
        fragments = entry.strip().split(": ")
        self.dairyDate = fragments[0]
        self.validFormats = DairyEntry.valid_formats(fragments[0])
        self.names = fragments[1].split(", ")

    def __str__(self):
        return f"{self.dairyDate} {self.validFormats} {self.names}"

    def has_name(self, name: str) -> bool:
        return name in self.names

    @staticmethod
    def valid_formats(d: str):
        return [f for f in ["%d-%m-%y", "%m-%d-%y", "%y-%d-%m", "%y-%m-%d"] if DairyEntry.valid_format(d, f)]

    @staticmethod
    def valid_format(d: str, f: str):
        try:
            datetime.strptime(d, f)
            return f
        except ValueError:
            return None

    # def parse_date(self, f: str) -> datetime | None:
    #     try:
    #         return datetime.strptime(self.dairyDate, f)
    #     except ValueError:
    #         return None


class Diary:
    def __init__(self, diary_entries: list[DairyEntry]):
        self.names = set(name
                      for de in diary_entries
                      for name in de.names)
        self.names_with_dates = defaultdict(list)
        for name, date in [(name, de.dairyDate)
                                 for de in diary_entries
                                 for name in self.names if de.has_name(name)]:
            self.names_with_dates[name].append(date)

        self.names_with_format = {}
        for (name, dates) in self.names_with_dates.items():
            self.names_with_format[name] = list(set.intersection(*map(set, [self.valid_formats(d) for d in dates])))[0]

    def names_at_date(self, date: datetime) -> list[str]:
        return [name for name in self.names
            if any(date == dd for dd in list(map(lambda d: datetime.strptime(d, self.names_with_format[name]), self.names_with_dates[name])))]

    @staticmethod
    def valid_formats(d: str):
        return [f for f in ["%d-%m-%y", "%m-%d-%y", "%y-%d-%m", "%y-%m-%d"] if DairyEntry.valid_format(d, f)]

with (open("resources/Puzzle9.txt") as puzzle_input):
    print(
        ' '.join(
            sorted(
                Diary([DairyEntry(line) for line in puzzle_input]).names_at_date(
                    datetime.strptime("11/09/2001", "%d/%m/%Y"))
            )
        )
    )
