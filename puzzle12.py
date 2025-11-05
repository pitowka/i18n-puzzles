# Ñíguez Peña, María de los Ángeles: 0151605
# English, Swedish, Dutch
from __future__ import annotations

from unidecode import unidecode
from functools import reduce
from typing import Callable
from unicodedata import normalize, combining


class User:
    def __init__(self, user: str):
        name, phone_number = user.strip().split(": ")
        self.last_name, self.first_name = name.split(", ")
        self.phone_number = phone_number

    def __repr__(self):
        return f"{self.last_name}, {self.first_name}: {self.phone_number}"

    def phone_number_as_int(self) -> int:
        return int(self.phone_number)

    def sorting(self, language: Callable[[str, str], str]) -> str:
        return language(self.first_name, self.last_name)


def english_normalize(s: str) -> str:
    return ''.join(c for c in unidecode(s.lower()) if c in 'abcdefghijklmnopqrstuvwxyz')

def english(fn: str, ln: str) -> str:
    return reduce(
        lambda acc, s: acc + ' ' + s,
        map(english_normalize, (ln, fn))
    )

def swedish_normalize(s: str) -> str:
    return ''.join(c for c in unidecode(
            s.upper()
            .replace("Å", "a")
            .replace("Æ", "ae")
            .replace("Ä", "ae")
            .replace("Ø", "o")
            .replace("Ö", "o"))
                   if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

def swedish(fn: str, ln: str) -> str:
    return reduce(
        lambda acc, s: acc + ' ' + s,
        map(swedish_normalize, (ln, fn))
    )


def dutch(fn: str, ln: str) -> str:
    return reduce(
        lambda acc, s: acc + ' ' + s,
        map(english_normalize, (ln[[i for i, c in enumerate(ln) if c.isupper()][0]::], fn))
    )


with open('resources/Puzzle12.txt') as puzzle_input_file:
    users = list(User(line) for line in puzzle_input_file)
    middle_index = len(users) // 2

    print(
        reduce(
            lambda acc, n: acc * n,
            (lu[middle_index].phone_number_as_int()
                for lu in (list(sorted(users, key=s))
                    for s in (lambda u: u.sorting(sorting)
                            for sorting in [english, swedish, dutch]
                    )
                )
             )
        )
    )
