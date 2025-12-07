from format_solutions import format_solution


def get_input(filename):
    with open(filename) as f:
        banks = [[int(n) for n in line] for line in f.read().splitlines()]
        return banks

def solve_part_1(banks):

    solution = 0

    for bank in banks:
        tens = max(bank[:-1])
        units = max(bank[bank.index(tens)+1:])
        n = 10 * tens + units
        solution += n

    return solution

def solve_part_2(banks):

    total_joltage = 0

    for bank in banks:

        joltage = 0
        position = 0

        for i in range(12):
            n = max(bank[position:i-11]) if i < 11 else max(bank[position:])
            position += bank[position:].index(n) + 1
            joltage += n * 10**(11-i)

        total_joltage += joltage

    return total_joltage

banks_ = get_input("input.txt")

if __name__ == "__main__":
    print(format_solution(solve_part_1(banks_), solve_part_2(banks_)))
