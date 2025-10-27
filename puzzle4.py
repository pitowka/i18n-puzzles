from datetime import datetime
from zoneinfo import ZoneInfo
import re

with (open("resources/Puzzle4.txt") as puzzle_input_file):
    p = re.compile(r"(Departure|Arrival):\s+(\S+)\s+(.+)")

    matches = [(m.group(2), m.group(3)) for m in \
        [p.match(sl) for sl in \
            [line.strip() for line in puzzle_input_file]] if m]

    dates = [datetime.strptime(m[1], "%b %d, %Y, %H:%M").replace(tzinfo=ZoneInfo(m[0])) for m in matches]

    print(
        sum(int((dates[i + 1] - dates[i]).total_seconds()/60) for i in range(0, len(dates), 2))
    )
