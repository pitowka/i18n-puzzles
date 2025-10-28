with open("resources/Puzzle5.txt") as puzzle_input_file:
    coordinate = 0
    shitPiles = 0

    for line in [line.rstrip("\n") for line in puzzle_input_file]:
        if line[coordinate % len(line)] == '💩':
            shitPiles += 1
        coordinate = coordinate + 2
    print(shitPiles)
