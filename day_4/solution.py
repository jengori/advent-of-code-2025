from format_solutions import format_solution


class Grid:
    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0])
        self.pad()


    def pad(self):
        self.rows.insert(0, ["."] * self.height)
        self.rows.append(["."] * self.height)

        for row in self.rows:
            row.insert(0, ".")
            row.append(".")

        self.height += 2
        self.width += 2


    def is_roll(self, pos: tuple) -> bool:
        if self.rows[pos[0]][pos[1]] == '@':
            return True
        else:
            return False

    @staticmethod
    def neighbours(pos: tuple):
        return [(pos[0] - 1, pos[1] - 1),
                (pos[0] - 1, pos[1]),
                (pos[0] - 1, pos[1] + 1),
                (pos[0], pos[1] - 1),
                (pos[0], pos[1] + 1),
                (pos[0] + 1, pos[1] - 1),
                (pos[0] + 1, pos[1]),
                (pos[0] + 1, pos[1] + 1)]

    def is_accessible(self, pos: tuple) -> bool:
            roll_count = 0
            for neighbour in self.neighbours(pos):
                if self.is_roll(neighbour):
                    roll_count += 1

            if roll_count < 4:
                return True
            return False

    def count_accessible_rolls(self):
        count = 0
        for row in range(1, self.height):
            for col in range(1, self.width):
                if self.is_roll((row, col)) and  self.is_accessible((row, col)):
                    count += 1

        return count

    def remove_accessible_rolls(self):
        removed = 0
        for row in range(1, self.height):
            for col in range(1, self.width):
                if self.is_roll((row, col)) and self.is_accessible((row, col)):
                    self.rows[row][col] = '.'
                    removed += 1

        return removed

    def max_removable_rolls(self):
        increasing = True
        total_removed = 0

        while increasing:
            removed = self.remove_accessible_rolls()
            total_removed += removed
            if removed == 0:
                increasing = False

        return total_removed

with open("input.txt") as f:
    lst_ = [[char for char in line] for line in f.read().splitlines()]

grid = Grid(lst_)

if __name__ == "__main__":
    print(format_solution(grid.count_accessible_rolls(), grid.max_removable_rolls()))
