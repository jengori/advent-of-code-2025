import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

shapes = []

for i, line in enumerate(lines[:29]):
    if re.match(r"^\d:", line):
        shapes.append([lines[i + 1], lines[i + 2], lines[i + 3]])

regions = []

for line in lines[30:]:
    regions.append([line.split(":")[0] , [int(n) for n in line.split(":")[1].strip().split(" ")]])

do_fit = 0
do_not_fit = 0

for region in regions:
    width = int(region[0][:2])
    height = int(region[0][3:])

    three_by_three_blocks = (width // 3) * (height // 3)

    if three_by_three_blocks >= sum (region[1]):
        do_fit += 1

    else:
        units_in_region = width * height

        min_units_needed = sum([region[1][j] * shapes[j][k].count('#') for k in range(3) for j in range(len(shapes))])

        if min_units_needed > units_in_region:
            do_not_fit += 1

print(f"Number that definitely do fit: {do_fit}")
print(f"Number that definitely don't fit: {do_not_fit}")
print(f"Because there are {do_fit} + {do_not_fit} = {len(regions)} regions ...\n")

print(f"Solution 1: {do_fit}")


