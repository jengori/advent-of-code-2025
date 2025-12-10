FILENAME = 'input.txt'

def get_input(filename):
    with open(filename) as f:
        return [(int(line.split(",")[0]), int(line.split(",")[1])) for line in f.read().splitlines()]

def get_max_area(lst: list[tuple]) -> int:
    max_area = 0

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                area = abs((lst[i][0] - lst[j][0] + 1) * (lst[i][1] - lst[j][1] + 1))
                if area > max_area:
                    max_area = area

    return max_area


reds = get_input(FILENAME)
part_1_solution = get_max_area(reds)
print(part_1_solution)