import re
from collections import Counter
from unicodedata import normalize, is_normalized

def valid_length(password: str):
    return 4 <= len(password) <= 12

def at_least_one_digit(password: str):
    return re.search(r"\d", password)

def at_least_one_vowel(password: str):
    return re.search(r"[aeiou]", normalized_string(password), flags=re.IGNORECASE)

def at_least_one_consonant(password: str):
    return re.search(r"[bcdfghjklmnpqrstvwxyz]", normalized_string(password), flags=re.IGNORECASE)

def no_recur(password: str):
    return Counter(c.lower() for c in list(normalized_string(password))
            if re.search(r"[a-z]", c, flags=re.IGNORECASE)).most_common(n=1)[0][1] == 1

def normalized_string(s):
    return normalize("NFKD", s).encode('ASCII', 'ignore').decode()


with open("resources/Puzzle8.txt") as puzzle_input:
    print(
        len(
            [sl for sl in [line.strip() for line in puzzle_input]
                if valid_length(sl)
                if at_least_one_digit(sl)
                if at_least_one_vowel(sl)
                if at_least_one_consonant(sl)
                if no_recur(sl)
             ]
        )
    )



