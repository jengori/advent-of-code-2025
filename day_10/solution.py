from itertools import combinations
from collections import Counter
FILENAME = 'input.txt'

def get_input(filename):
    with open(FILENAME) as f:
        return f.read().splitlines()

total_presses = 0
machines = get_input(FILENAME)

for m, machine in enumerate(machines):
    match_found = False
    light_diagram = [False if char == '.' else True for char in machine[1 :machine.index(']')]]
    buttons = [button if type(button) == tuple else (button,) for button in [eval(s) for s in machine[machine.index('('):machine.index('{') - 1].split(' ')]]

    min_presses = len(buttons)

    for n in range(1, len(buttons)):
        combs = combinations(buttons, n)

        for comb in combs:
            counts = Counter(x for button in comb for x in button)

            lights = [False] * len(light_diagram)

            for key in counts:

                if counts[key] % 2 == 1:
                    lights[key] = True

            if lights == light_diagram:
                if len(comb) < min_presses:
                    min_presses = len(comb)

    total_presses += min_presses

print(f"Part 1 solution: {total_presses}")
