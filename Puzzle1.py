"""
Price is 13 if both are in limit range
"""
class PuzzleMessage:
    def __init__(self, message):
        self.message = message.strip()

    """
    max 140 and price is 7
    """
    def characters_count(self) -> int:
        return len(self.message)

    """
    max 160 and price is 11
    """
    def bytes_count(self) -> int:
        return len(self.message.encode('utf-8'))

    def price(self) -> int:
        if self.characters_count() in range(140 + 1) and self.bytes_count() in range(160 + 1):
            return 13
        elif self.characters_count() in range(140 + 1):
            return 7
        elif self.bytes_count() in range(160 + 1):
            return 11
        else:
            return 0

with open("resources/Puzzle1.txt") as input_puzzle:
    print(
        sum(
            PuzzleMessage(line).price()
                for line in input_puzzle
        )
    )