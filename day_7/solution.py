from format_solutions import format_solution

FILENAME="input.txt"


class Manifold:
    def __init__(self, grid):
        self.grid = grid
        self.s_col = grid[0].index("S")
        self.width = self.height = len(self.grid)

    def solve(self):
        current = [0] * self.width
        current[self.s_col] = 1

        splits = 0

        for i in range(self.height - 1):
            nxt = [0] * self.width
            row = self.grid[i + 1]

            for j in range(self.width):
                count = current[j]
                if count == 0:
                    continue

                if row[j] != "^":
                    nxt[j] += count
                else:
                    nxt[j - 1] += count
                    nxt[j + 1] += count
                    splits += 1

            current = nxt

        return splits, sum(current)


with open(FILENAME) as f:
    grid_ = [[char for char in line] for line in f.read().splitlines()]
    manifold = Manifold(grid_)

if __name__ == "__main__":
    solutions = manifold.solve()
    print(format_solution(solutions[0], solutions[1]))