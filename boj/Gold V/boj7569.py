"""
[ 설명 ]
인접한 토마토끼리는 익는다
인접한 것은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 토마토 를 의미
대각선은 영향을 주지 못함
혼자 저절로 익는 경우는 없다

창고에 있는 토마토들이 며칠이 지나면 다 이게 되는지 그 최소 일수를 알고 ㅅ피다

단, 일부 상자에는 토마토가 들어있지 않을 수 있다.

[ 입력 ]
M, N, H
M은 상자의 가로, N은 상자의 세로, H는 상자의 높이
둘째 줄 부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가
주어진다.
즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토 정보가 주어짐
각 줄에는 상자 가로 줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토
정수 -1은 토마토가 드렁있지 않은 칸을 나타냄
이러한 N개의 줄이 H번 반복하여 주어짇나.

토마토가 하나 이상 있는 경우만 입력으로 주어짐

[ 출력 ]
토마토가 모두 익을때 까지 며칠이 걸리는지 계산해서 출력
저장될때부터 모두 익었다면, 0을
토마토가 모두 익지 못하는 상황이면 -1을 출력
"""

import sys

from collections import deque


def bfs(graph, m, n, h):
    q = deque([])
    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    all_check = m * n * h
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if visited[i][j][k]:
                    continue
                if graph[i][j][k] == 1:
                    q.append((i, j, k))
                    visited[i][j][k] = True
                    all_check -= 1
                elif graph[i][j][k] == -1:
                    all_check -= 1
    if all_check == 0:
        return 0
    day = 0
    while q:
        z, y, x = q.popleft()
        for idx in range(6):
            nz = z + dz[idx]
            ny = y + dy[idx]
            nx = x + dx[idx]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if visited[nz][ny][nx]:
                    continue
                if graph[nz][ny][nx] == 0:
                    q.append((nz, ny, nx))
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    visited[nz][ny][nx] = True
                    all_check -= 1
        if day < graph[z][y][x]:
            day = graph[z][y][x] - 1
    if all_check == 0:
        return day
    else:
        return -1


input = sys.stdin.readline

M, N, H = map(int, input().split(" "))
tomato_box = []

for i in range(H):
    tomato_box.append([])
    for j in range(N):
        tomato_box[i].append(list(map(int, input().split(" "))))
print(bfs(tomato_box, M, N, H))
