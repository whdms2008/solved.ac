from collections import defaultdict
from sys import stdin


def DFS(v, visited, graph):
    visited.add(v)
    for w in graph[v]:
        if w not in visited:
            DFS(w, visited, graph)


N = int(stdin.readline())
M = int(stdin.readline())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
DFS(1, visited, graph)
print(len(visited) - 1)
