class Grid:

    OFFSETS = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1), (0, 1),
               (1, -1), (1, 0), (1, 1)]

    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0])
        self.pad()

        self.rolls = {(r, c)
                      for r in range(self.height)
                      for c in range(self.width)
                      if self.rows[r][c] == '@'}

    def pad(self):
        self.rows.insert(0, ["."] * self.height)
        self.rows.append(["."] * self.height)

        for row in self.rows:
            row.insert(0, ".")
            row.append(".")

        self.height += 2
        self.width += 2


    def is_accessible(self, pos):
        r, c = pos
        count = sum((r+dr, c+dc) in self.rolls for dr, dc in self.OFFSETS)
        return count < 4

    def count_accessible_rolls(self):
        return sum(self.is_accessible(rc) for rc in self.rolls)

    def remove_accessible_rolls(self):
        removable = {pos for pos in self.rolls if self.is_accessible(pos)}
        for (r, c) in removable:
            self.rows[r][c] = '.'
        self.rolls -= removable
        return len(removable)

    def max_removable_rolls(self):
        total = 0
        while True:
            removed = self.remove_accessible_rolls()
            if removed == 0:
                break
            total += removed
        return total

if __name__ == '__main__':
    with open("input.txt") as f:
        lst_ = [[char for char in line] for line in f.read().splitlines()]

    grid = Grid(lst_)

    print(f"Part 1 solution: {grid.count_accessible_rolls()}")
    print(f"Part 2 solution: {grid.max_removable_rolls()}")
