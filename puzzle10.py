import unicodedata
import bcrypt

def password_variations(s: str) -> list[str]:
    result = [""]
    for c in unicodedata.normalize("NFC", s):
        decomposed = unicodedata.normalize("NFD", c)
        if decomposed == c:
            result = [r + c for r in result]
        else:
            result = [r + c for r in result] + [r + decomposed for r in result]
    return result


with open("resources/Puzzle10.txt") as puzzle_input_file:
    passwords, attempts = puzzle_input_file.read().split("\n\n")
    users = {user: h for user, h in map(str.split, passwords.splitlines())}

    print(
        len(
            list(
                user for user, passwd in map(str.split, attempts.splitlines())
                    if any(bcrypt.checkpw(v.encode(), users[user].encode())
                           for v in password_variations(passwd))
            )
        )
    )

