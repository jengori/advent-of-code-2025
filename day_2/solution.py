import bisect

def in_ranges(n: int, ranges: list[tuple]) -> bool:
    """
    Returns True if an integer n is in any of the (inclusive, sorted, non-overlapping) list of ranges;
    else returns False.
    """

    starts = [r[0] for r in ranges]
    ends = [r[1] for r in ranges]

    i = bisect.bisect_right(starts, n) - 1
    return i >= 0 and n <= ends[i]

def solve(invalid_ids: list[int]) -> int:
    """Returns the solution for a given list of invalid ids."""

    with open("input.txt") as f:
        ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in f.read().split(",")]
        ranges.sort(key=lambda x: (x[0]))

    solution = 0

    for invalid_id in invalid_ids:
        if in_ranges(invalid_id, ranges):
            solution += invalid_id

    return solution


def make_list(part: int) -> list[int]:
    """Constructs a list of invalid ids for Part 1 or Part 2 of the puzzle."""
    if part == 1:
        lst = [m * (10 ** n + 1)
               for n in range(1, 6)
               for m in range(10 ** (n - 1), 10 ** n)]

        return lst

    elif part == 2:
        lst = list(set([int(m * (10 ** (k * n) - 1) / (10 ** k - 1))
                        for k in range(1, 6)
                        for m in range(10 ** (k - 1), 10 ** k)
                        for n in range(2, 10 // k + 1)]))

        return lst

if __name__ == "__main__":
    print(f"Part 1 solution: {solve(make_list(1))}")
    print(f"Part 2 solution: {solve(make_list(2))}")
