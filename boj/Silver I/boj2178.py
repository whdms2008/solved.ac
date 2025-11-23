"""
| 설명 |

NxM크기의 배열로 표현되는 미로가 있다.

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는
최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동ㅎ알 수 있다.
"""

"""
[ 입력 ]
첫째 줄에 두 정수 N, M(2<=N, M <= 100)이 주어진다.
다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
각각의 수들은 붙어서 입력으로 주어진다.
"""

"""
[ 출력 ]
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다.
항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
"""

from collections import deque


def bfs(graph, N, M):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        if x == M - 1 and y == N - 1:
            return graph[y][x]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((nx, ny))


N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(maze, N, M))
