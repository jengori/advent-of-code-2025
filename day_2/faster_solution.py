import bisect

# Construct lists of invalid IDs for Part 1 and Part 2
part_1_invalid_ids = []
part_2_invalid_ids = []

for n in range(1, 10):
    part_1_invalid_ids.append(int(str(n)*2))

    for i in (2, 3, 5, 7):
        part_2_invalid_ids.append(int(str(n)*i))

for n in range(10, 100):
    part_1_invalid_ids.append(int(str(n)*2))

    for i in (2, 3, 5):
        part_2_invalid_ids.append(int(str(n)*i))

for n in range(100, 1000):
    part_1_invalid_ids.append(int(str(n)*2))

    for i in (2, 3):
        part_2_invalid_ids.append(int(str(n)*i))

for n in range(1000, 10000):
    part_1_invalid_ids.append(int(str(n)*2))
    part_2_invalid_ids.append(int(str(n)*2))

for n in range(10000, 100000):
    part_1_invalid_ids.append(int(str(n)*2))
    part_2_invalid_ids.append(int(str(n)*2))

part_2_invalid_ids = list(set(part_2_invalid_ids))

# Read input and format as sorted list of tuples
with open("input.txt") as f:
    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in f.read().split(",")]
    ranges.sort(key=lambda x: (x[0]))

starts = [r[0] for r in ranges]
ends = [r[1] for r in ranges]

def in_ranges(n):
    """
    Returns True if an integer n is in any of the (inclusive, non-overlapping) ranges in the input file;
    else returns False.
    """

    i = bisect.bisect_right(starts, n) - 1
    return i >= 0 and n <= ends[i]

# Calculate and print solutions for part 1 and part 2

part_1_solution = 0
for invalid_id in part_1_invalid_ids:
    if in_ranges(invalid_id):
        part_1_solution += invalid_id

part_2_solution = 0
for invalid_id in part_2_invalid_ids:
    if in_ranges(invalid_id):
        part_2_solution += invalid_id

print(f"Part 1 solution: {part_1_solution}")
print(f"Part 2 solution: {part_2_solution}")
