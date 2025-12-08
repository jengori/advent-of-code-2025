import numpy as np
from scipy.spatial import KDTree
from solution_part_2 import solution_2
from format_solutions import format_solution

with open("input.txt") as f:
    points_ = np.array([list(map(int, l.split(","))) for l in f])

def closest_pairs(points, k=1000):
    tree = KDTree(points)
    seen, pairs = set(), []

    for i, p in enumerate(points):
        d, idx = tree.query(p, min(len(points), k + 5))
        for dist, j in zip(d[1:], idx[1:]):
            pair = tuple(sorted((i, j)))
            if pair not in seen:
                seen.add(pair)
                pairs.append((dist, i, j))

    return sorted(pairs)[:k]

def components(n, pairs):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    for _, a, b in pairs:
        union(a, b)

    comp = {}
    for i in range(n):
        r = find(i)
        comp.setdefault(r, []).append(i)

    return list(comp.values())

if __name__ == "__main__":

    pairs_ = closest_pairs(points_)
    circuits = components(len(points_), pairs_)

    circuits.sort(key=len, reverse=True)
    solution = len(circuits[0]) * len(circuits[1]) * len(circuits[2])

    print(format_solution(solution, solution_2))
