import numpy as np

FILENAME = "input.txt"

def get_input(filename):
    with open("input.txt") as f:
        points = np.array([list(map(int, l.split(","))) for l in f])
        return points


points_ = get_input(FILENAME)
diff = points_[:, None, :] - points_[None, :, :]
dists = np.sqrt((diff ** 2).sum(axis=-1))

np.fill_diagonal(dists, np.inf)

pairs = []
for i in range(len(dists)):
    for j in range(len(dists[0])):
        pairs.append((dists[i][j], i, j))

pairs.sort(key=lambda x: x[0])

points_in_circuit = set()

i = 0
while len(points_in_circuit) < 1000:
    idx1 = pairs[i][1]
    idx2 = pairs[i][2]
    points_in_circuit.add(idx1)
    points_in_circuit.add(idx2)
    i += 1

solution_2 = points_[idx1][0] * points_[idx2][0]
