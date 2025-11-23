from collections import deque


def bfs(graph, n):
    q = deque([])
    visited = [[False] * n for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    colors = {"R": 0, "G": 0, "B": 0}
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q.append((j, i))
                while q:
                    x, y = q.popleft()
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if 0 <= nx < n and 0 <= ny < n:
                            if visited[ny][nx]:
                                continue
                            if graph[i][j] != graph[ny][nx]:
                                continue
                            q.append((nx, ny))
                            visited[ny][nx] = True
                colors[graph[i][j]] += 1
    return colors.values()


N = int(input())

rgb_matrix = [input() for _ in range(N)]
rb_matrix = [line.replace("G","R") for line in rgb_matrix.copy()]

rgb_sum = sum(bfs(rgb_matrix, N))
rb_sum = sum(bfs(rb_matrix, N))
print(rgb_sum, rb_sum)