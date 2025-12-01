class Dial:
    def __init__(self, highest = 99, start_pos=50):
        self.limit = highest
        self.pos = start_pos

    def move(self, rotation: int):
        self.pos = ((self.pos + rotation) % (self.limit + 1))

    def is_set_to_zero(self):
        return self.pos == 0

    def set_pos(self, n):
        self.pos = n

    def solve_part_1(self, rotations: list):
        password = 0

        for rotation in rotations:
            self.move(rotation)

            if self.is_set_to_zero():
                password += 1

        return password

    def solve_part_2(self, rotations: list):
        password = 0

        for rotation in rotations:
            password += abs(rotation) // (self.limit + 1)

            start_pos = self.pos
            self.move(rotation)
            end_pos = self.pos

            if abs(rotation) % (self.limit + 1) != 0 and start_pos != 0:

                if rotation > 0 and end_pos < start_pos:
                    password += 1
                elif rotation < 0 and (end_pos > start_pos or end_pos == 0):
                    password += 1

        return password


with open('input.txt', 'r') as f:
    r = [int(line.strip()[1:]) if line[0] == "R" else -int(line.strip()[1:])  for line in f.readlines()]

dial = Dial()
print(f"Part 1 solution: {dial.solve_part_1(r)}")
dial.set_pos(50)
print(f"Part 2 solution: {dial.solve_part_2(r)}")
