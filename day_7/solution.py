FILENAME="input.txt"

class Manifold:
    def __init__(self, grid):
        self.grid = grid
        self.start_pos = (0, grid[0].index("S"))
        self.beams = {self.start_pos}
        self.splits = 0

        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def move(self):
        new_beams = set()
        for beam in self.beams:
            if self.grid[beam[0] + 1][beam[1]] != "^":
                new_beams.add((beam[0] + 1, beam[1]))
            else:
                new_beams.add((beam[0] + 1, beam[1] - 1))
                new_beams.add((beam[0] + 1, beam[1] + 1))
                self.splits += 1

        self.beams = new_beams

    def solve_part_1(self):
        for _ in range(self.height - 1):
            self.move()
        return self.splits

    def solve_part_2(self):
        current = [0] * self.width
        current[self.start_pos[1]] = 1

        for i in range(self.height - 1):
            nxt = [0] * self.width
            row = manifold.grid[i + 1]

            for j in range(self.width):
                count = current[j]
                if count == 0:
                    continue

                if row[j] != "^":
                    nxt[j] += count
                else:
                    nxt[j - 1] += count
                    nxt[j + 1] += count

            current = nxt

        possible_worlds = sum(current)
        return possible_worlds



with open(FILENAME) as f:
    grid_ = [[char for char in line] for line in f.read().splitlines()]

manifold = Manifold(grid_)
print(f"Part 1 solution: {manifold.solve_part_1()}")
print(f"Part 2 solution: {manifold.solve_part_2()}")
