import numpy as np
import solution_part_2
from format_solutions import format_solution

FILENAME = "input.txt"

def read_input(filename):
    with (open(filename) as f):
        lines = f.readlines()

    number_lines = [line.strip() for line in lines[:-1]]
    operators_line = lines[-1]

    return number_lines, operators_line

def sums(filename):
    number_lines, operators_line = read_input(filename)
    operators = operators_line.split()
    numbers = [[int(x) for x in line.split()] for line in number_lines]
    numbers_transposed = np.transpose(numbers)

    sums = []
    for i, operator in enumerate(operators):
        sums.append((operator, numbers_transposed[i]))

    return sums

def solve(filename):
    total = 0
    for sum_ in sums(filename):
        operator = sum_[0]

        if operator == "+":
            total += np.sum(sum_[1])

        elif operator == "*":
            total += np.prod(sum_[1])

    return total

if __name__ == "__main__":
    print(format_solution(solve(FILENAME), solution_part_2.total))
