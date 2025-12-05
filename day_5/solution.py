FILENAME = 'input.txt'

def merge_overlapping(lst:list[tuple[int, int]]) -> list[tuple[int, int]]:
    lst.sort()
    res = []

    for i, r in enumerate(lst):
        start = r[0]
        end = r[1]

        if res and res[-1][1] >= end:
            continue

        for j, s in enumerate(lst, start=1):
            if s[0] <= end:
                end = max(end, s[1])

        res.append((start, end))

    return res

def get_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    ranges = [(int(line.split('-')[0]), int(line.split('-')[1])) for line in lines if '-' in line]

    ingredients = [int(line) for line in lines if '-' not in line and line != '']

    return ranges, ingredients

def solve_part_1():
    ranges, ingredients = get_input(FILENAME)
    fresh = 0

    for ingredient in ingredients:
        for ran in ranges:
            if ran[0] <= ingredient <= ran[1]:
                fresh += 1
                break

    return fresh

def solve_part_2():
    ranges = get_input(FILENAME)[0]
    merged_ranges = merge_overlapping(ranges)
    fresh = 0

    for range_ in merged_ranges:
        fresh += range_[1] - range_[0] + 1

    return fresh

if __name__ == '__main__':
    print(f'Part 1 solution: {solve_part_1()}')
    print(f'Part 2 solution: {solve_part_2()}')
