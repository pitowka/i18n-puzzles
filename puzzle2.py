import datetime
from collections import Counter

with open("resources/Puzzle2.txt") as puzzle_input:
    stats = Counter(
        map(
            datetime.datetime.fromisoformat,
            map(str.strip, [line for line in puzzle_input])
        )
    )

    print(
        max(stats, key = stats.get)
            .astimezone(datetime.timezone.utc)
            .isoformat()
    )

with open("resources/Puzzle2.txt") as puzzle_input:
    print(
        max(
            Counter(
                map(
                    datetime.datetime.fromisoformat,
                    map(str.strip, [line for line in puzzle_input])
                )
            ).items()
            , key = lambda d: d[1]
        )[0].astimezone(datetime.timezone.utc)
        .isoformat()
    )


with open("resources/Puzzle2.txt") as puzzle_input:
    print(
        Counter(
            map(
                datetime.datetime.fromisoformat,
                map(str.strip, [line for line in puzzle_input])
            )
        ).most_common(1)[0][0]
        .astimezone(datetime.timezone.utc)
        .isoformat()
    )