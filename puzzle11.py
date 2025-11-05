def rotate(s: str, i: int) -> str:
    alphabet = 'αβγδεζηθικλμνξοπρστυφχψω'
    new_alphabet = alphabet[i:] + alphabet[:i]

    result = ''
    for c in s:
        result += c if c not in alphabet else new_alphabet[alphabet.index(c)]
    return result

def find_odysseus(s: str) -> int:
    odysseuses = [o.lower() for o in ['Οδυσσευς', 'Οδυσσεως', 'Οδυσσει', 'Οδυσσεα', 'Οδυσσευ']]

    for i in range(24):
        if any(o in rotate(s, i) for o in odysseuses):
            return i
    else:
        return 0

with open('resources/Puzzle11.txt') as puzzle_input_file:
    print(
        sum(
            find_odysseus(line.strip().lower()) for line in puzzle_input_file
        )
    )

