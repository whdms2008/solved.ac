from sys import stdin
from collections import defaultdict


def DFS(start, graph, visited):
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


T = int(stdin.readline())
Field = [[] for i in range(T)]
cnt = [0] * T
for i in range(T):
    M, N, K = map(int, stdin.readline().split(" "))

    for _ in range(K):
        X, Y = map(int, stdin.readline().split(" "))
        Field[i].append([X, Y])

    Field[i].sort()
    graph = defaultdict(set)
    for x, y in Field[i]:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if [nx, ny] in Field[i]:
                graph[(x, y)].add((nx, ny))

    visited_total = set()
    for point in Field[i]:
        if tuple(point) not in visited_total:
            visited = DFS(tuple(point), graph, set())
            visited_total.update(visited)
            cnt[i] += 1
for i in cnt:
    print(i)
