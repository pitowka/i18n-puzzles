import re
from unicodedata import normalize, is_normalized


def valid_length(password: str):
    return 4 <= len(password) <= 12

def at_least_one_digit(password: str):
    return re.search(r"\d", password)

def at_least_one_upper(password: str):
    return re.search(r"[A-Z]", normalized_string(password))

def at_least_one_lower(password: str):
    return re.search(r"[a-z]", normalized_string(password))

def normalized_string(s):
    return normalize("NFKD", s).encode('ASCII', 'ignore').decode()

with open("resources/Puzzle3.txt") as puzzle_input:
    print(
        len(
            [sl for sl in [line.strip() for line in puzzle_input]
                if valid_length(sl)
                if at_least_one_digit(sl)
                if at_least_one_upper(sl)
                if at_least_one_lower(sl)
                if not is_normalized("NFKD", sl)
             ]
        )
    )

