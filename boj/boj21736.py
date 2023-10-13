from sys import stdin
from collections import deque

N, M = list(map(int, stdin.readline().split()))


def bfs(graph, root):
    visited = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(set(graph[node]) - set(visited))
    return visited


graph = {
    'I': ['A', 'B'],
    'A': ['I', 'P', 'C'],
    'B': ['I', 'P'],
    'C': ['A', 'D'],
    'D': ['P', 'C', 'P2'],
    'P': ['A', 'B', 'D'],
    'P2': ['D']
}
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
g = list((stdin.readline().strip() for _ in range(N)))
print(g)
i_pos = (0, 0)
for i in range(N):
    if "I" in g[i]:
        for j in range(M):
            print(i, g[i].find("I"))
            i_pos = (i, g[i].find("I"))
            break
print(f"I 위치 : {i_pos}")
cnt = 0
visit = []
for i in direction:
    x_pos = i_pos[0] + i[0]
    if x_pos < 0 or x_pos >= M:
        continue
    y_pos = i_pos[1] + i[1]
    if y_pos < 0 or y_pos >= N:
        continue
    print(f"위치 {chr(65 + cnt)} ", x_pos, y_pos)
    visit.append((x_pos, y_pos))
    cnt += 1
print(sum('p' in i.lower() for i in bfs(graph, 'I')))  # ['A', 'B', 'C', 'D', 'E', 'F']
