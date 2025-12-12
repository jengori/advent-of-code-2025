def count_paths(graph, start, end):
    memo = {}

    def dfs(node):
        if node == end:
            return 1

        if node in memo:
            return memo[node]

        total = 0
        for neighbor in graph[node]:
            total += dfs(neighbor)

        memo[node] = total
        return total

    return dfs(start)


with open('input.txt', 'r') as f:
    graph_ = {line.strip().split(":")[0]: line.strip().split(":")[1][1::].split(" ") for line in f.readlines()}

print(f"Part 1 solution: {count_paths(graph_, "you", "out")}")
