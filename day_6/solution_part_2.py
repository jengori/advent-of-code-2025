import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

lines_to_lists = [[x for x in list(line) if x != '\n'] for line in lines]

max_line_length = len(max(lines_to_lists, key=len))

for line in lines_to_lists:
    if len(line) != max_line_length:
        for i in range(max_line_length - len(line)):
            line.append(" ")

lines_transposed = np.transpose(lines_to_lists)

sums = []
line_num = 0

while line_num < len(lines_transposed):
    n_as_string  = ''.join([x for x in lines_transposed[line_num] if x.isdigit()])
    if n_as_string != '':
        n = int(n_as_string)

    if '+' in lines_transposed[line_num]:
        sums.append(('+', []))
        sums[-1][1].append(n)
        line_num += 1
    elif '*' in lines_transposed[line_num]:
        sums.append(('*', []))
        sums[-1][1].append(n)
        line_num += 1
    else:
        if ''.join([x for x in lines_transposed[line_num] if x.isdigit()]) != '':
            if n:
                sums[-1][1].append(n)
        line_num += 1

total = 0
for sum_ in sums:
    if sum_[0] == '+':
        total += np.sum(sum_[1])
    else:
        total += np.prod(sum_[1])
