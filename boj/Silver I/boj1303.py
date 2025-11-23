"""
[ 문제 ]
N명이 뭉쳐있을때는 N**2의 위력을 낼 수 있다


"""

"""
[ 입력 ]
첫째 줄에는 전쟁터 가로 크기 N, 세로 M (1<=N, M<=100)이 주어진다.
두번째 줄에서 M+1번재 줄에는 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다.
모든 자리에는 병사가 한명 있다. B는 파란색, W는 흰색이다.
"""

"""
[ 첫 번째 줄에 당신의 병사의 위력의 합과 적구의 병사의 위력의 합을 출력한다 ]
"""

from collections import deque


def bfs(graph, n, m):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    powers = [0, 0]
    for i in range(m):
        for j in range(n):
            if graph[i][j] != "X":
                target = graph[i][j]
                q = deque([(j, i)])
                visited = [(j, i)]
                while q:
                    x, y = q.popleft()
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]

                        if (nx, ny) in visited:
                            continue
                        if 0 <= nx < n and 0 <= ny < m:
                            if graph[ny][nx] == target:
                                q.append((nx, ny))
                                visited.append((nx, ny))
                for x, y in visited:
                    graph[y][x] = "X"
                powers[0 if target == "W" else 1] += len(visited) ** 2
    return powers


N, M = map(int, input().split(" "))

matrix = [list(input()) for _ in range(M)]

W, B = bfs(matrix, N, M)
print(W, B)