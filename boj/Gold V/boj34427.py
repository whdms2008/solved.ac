import sys
from collections import deque

input = sys.stdin.readline
N, M, x, y = map(int, input().split(" "))

matrix = [list(map(int, input().split(" "))) for _ in range(M)]


def dfs(graph, n, m, x, y):
    q = deque([(x, y)])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    target = graph[y][x]

    visited = {(x, y)}
    while q:
        curr_x, curr_y = q.popleft()

        for idx in range(4):
            nx = curr_x + dx[idx]
            ny = curr_y + dy[idx]
            if (nx, ny) in visited:
                continue
            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == target:
                    q.append((nx, ny))
                    visited.add((nx, ny))

    return visited

for coord in sorted(dfs(matrix, N, M, x, y), key=lambda pos: (pos[1], pos[0])):
    print(*coord)
