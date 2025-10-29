import re

class Words:
    def __init__(self, words):
        self.words = [self.__transform(idx + 1, w) for idx, w in enumerate(words)]

    @staticmethod
    def __transform(idx, w)->str:
        if idx % 15 == 0:
            return w.encode("latin-1").decode("utf-8").encode("latin-1").decode("utf-8")
        elif idx % 5 == 0 or idx % 3 == 0:
            return w.encode("latin-1").decode("utf-8")
        else:
            return w

    def position_of_pattern(self, pattern)->int:
        return next((idx + 1 for idx, w in enumerate(self.words) if re.compile(f"^{pattern}$").match(w)), None)

class CrossWords:
    def __init__(self, patterns):
        self.patterns = patterns

    def solution(self, words: Words)->int:
        return sum(words.position_of_pattern(p) for p in self.patterns)

with open("resources/Puzzle6.txt") as puzzle_input_file:
    file_lines = [line.strip() for line in puzzle_input_file]
    print(
        CrossWords(file_lines[file_lines.index('') + 1:])
            .solution(Words(file_lines[:file_lines.index('')]))
    )
