import re


class JapaneseNumber:
    def __init__(self, number):
        self.number = number

    order_of_magnitude = {
        '十': 10,
        '百': 100,
        '千': 1000,
        '万': 10000,
        '十万': 100000,
        '百万': 1000000,
        '千万': 10000000,
        '億': 10000000
    }

    numerals = {
        '一': 1,
        '二': 2,
        '三': 3,
        '四': 4,
        '五': 5,
        '六': 6,
        '七': 7,
        '八': 8,
        '九': 9
    }

    base = 10 / 33

    units_of_length = {
        '尺': 1 * base,
        '丈': 10 * base,
        '町': 360 * base,
        '里': 12960 * base,
        '毛': 1 / 10000 * base,
        '厘': 1 / 1000 * base,
        '分': 1 / 100 * base,
        '寸': 1 / 10 * base
    }

    def value_in_meters(self) -> int:
        return 10

with open("resources/Puzzle14.txt") as puzzle_input_file:
    print(
        sum(jp1.value_in_meters() * jp2.value_in_meters()
            for jp1, jp2 in ((JapaneseNumber(n1), JapaneseNumber(n2))
                for n1, n2 in (line.strip().split(' × ')
                    for line in puzzle_input_file))))



print(JapaneseNumber('三百七十四万二千五百三十厘').value_in_meters())


urob to na 2x
najskor oddel units_of_length a potom x-krat zopakuj \d[a-z] like pattern

for x in re.finditer(r"((?:([一二三四五六七八九])+(十|百|千|万|十万|百万|千万|億)*)+)+?([尺丈町里毛厘分寸])", '三百七十四万二千五百三十厘'):
    print(x.groups())

