import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

max_val = 0

max_element = max(map(max, matrix))


def dfs(x, y, cnt, total):
    global max_val

    if total + (4 - cnt) * max_element <= max_val:
        return

    if cnt == 4:
        max_val = max(max_val, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(nx, ny, cnt + 1, total + matrix[ny][nx])
                visited[ny][nx] = False


def check_exception(x, y):
    global max_val
    center = matrix[y][x]
    neighbors = []

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            neighbors.append(matrix[ny][nx])

    if len(neighbors) < 3:
        return

    if len(neighbors) == 3:
        max_val = max(max_val, center + sum(neighbors))
    else:
        max_val = max(max_val, center + sum(neighbors) - min(neighbors))


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(j, i, 1, matrix[i][j])
        visited[i][j] = False

        check_exception(j, i)

print(max_val)