def solve(ranges: list[tuple], part: int):
    all_invalid = []

    for r in ranges:
        invalid = []

        for n in range(r[0], r[1] + 1):
            n_as_string = str(n)
            l = len(n_as_string)

            if l % 2 == 0:
                split = int(l / 2)

                if n_as_string[0:split] == n_as_string[split:]:
                    invalid.append(n)

            if part == 2:
                if l != 1 and l % 2 != 0 and len(set(n_as_string)) == 1:
                    if n not in invalid:
                        invalid.append(n)

                if l == 6 and n_as_string[0:2] == n_as_string[2:4] == n_as_string[4:]:
                    if n not in invalid:
                        invalid.append(n)

                elif l == 8 and n_as_string[0:2] == n_as_string[2:4] == n_as_string[4:6] == n_as_string[6:]:
                    if n not in invalid:
                        invalid.append(n)

                elif l == 9 and n_as_string[0:3] == n_as_string[3:6] == n_as_string[6:]:
                    if n not in invalid:
                        invalid.append(n)

                elif l == 10 and n_as_string[0:2] == n_as_string[2:4] == n_as_string[4:6] == n_as_string[6:8] == n_as_string[8:]:
                    if n not in invalid:
                        invalid.append(n)

        for invalid_id in invalid:
            all_invalid.append(invalid_id)

    return sum(all_invalid)

with open("input.txt") as f:
    ranges_ = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in f.read().split(",")]

print(f"Part 1 solution: {solve(ranges_, 1)}")
print(f"Part 2 solution: {solve(ranges_, 2)}")
