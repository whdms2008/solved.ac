"""
[ 문제 ]
연결된 가장 큰 음식물의 개수를 찾아라

[ 입력 ]
세로 길이 N
1 <= N <= 100
가로 길이 M
1 <= M <= 100
그리고 음식물 쓰레기의 개수 K
1 <= K <= N*M 이 주어진다.
K개의 줄에 음식물이 떨어진 조표 r,c가 주어진다.

[ 출력 ]
- 가장 큰 음식물의 크기를 출력
"""
import sys
from collections import deque


def bfs(graph, n, m):
    q = deque([])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[False] * m for _ in range(n)]
    max_food = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == -1 and not visited[i][j]:
                q.append((j, i))
                visited[i][j] = True
                curr_food = 1
                while q:
                    x, y = q.popleft()

                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]

                        if 0 <= ny < n and 0 <= nx < m:
                            if graph[ny][nx] != -1:
                                continue
                            if visited[ny][nx]:
                                continue
                            q.append((nx, ny))
                            visited[ny][nx] = True
                            curr_food += 1
                if max_food < curr_food:
                    max_food = curr_food
    return max_food


input = sys.stdin.readline

N, M, K = map(int, input().split(" "))

matrix = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split(" "))
    matrix[r - 1][c - 1] = -1

print(bfs(matrix, N, M))
