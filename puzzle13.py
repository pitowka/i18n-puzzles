import re

class WordsWithIndex:
    def __init__(self, words_in_str: str):
        self.words = [(i, w)
            for i, ww in enumerate(words_in_str.splitlines())
            for w in self.decode(ww)][::-1]
    # try words from end of list

    @staticmethod
    def decode(s: str) -> list[str]:
        b = bytes.fromhex(s)

        if s.startswith("fffe") or s.startswith("feff"):
            return [b.decode("utf-16")]
        elif s.startswith("efbbbf"):
            return [b.decode("utf-8-sig")]

        result = []
        for encoding in ("utf-8", "utf-16-le", "utf-16-be", "latin-1"):
            try:
                decoded = b.decode(encoding)
            except:
                continue

            if not any(bad in decoded for bad in ("©", "\ufeff", "¶", "Ã¤", "Ã\x9f", "\0")):
                result.append(decoded)

        assert result, f"failed to decode {s}"
        return result
    
    def position_of_pattern(self, pattern)->int:
        print([w for idx, w in self.words if re.compile(f"^{pattern}$").match(w)])

        return next((idx + 1 for idx, w in self.words if re.compile(f"^{pattern}$").match(w)), None)

class CrossWords:
    def __init__(self, patterns: list[str]):
        self.patterns = [p.strip() for p in patterns]

    def solution(self, words_with_index: WordsWithIndex)->int:
        return sum(words_with_index.position_of_pattern(p) for p in self.patterns)


with open('resources/Puzzle13.txt') as puzzle_input_file:
    words, cross_word = puzzle_input_file.read().split('\n\n')

    print(
        CrossWords(cross_word.splitlines())
            .solution(WordsWithIndex(words))
    )
