# 고랭지에서 유기농 배추를 재배하기로 하였다.
# 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에
# 한나는 해충 방지에 효괒거인 배추흰지렁이를 구입 하기로 결심했다.
# 이 지ㅓㅇ이는 배추 근처에 서식하며 인접한 다른 배추로 이동할 수 있다
# 그 배추들 역시 해추으롭터 보호받을 수 있다.
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우 서로 인접해 있는 것이다.
# 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다
# 배추들이 모여있는 곳에는 배추흰 지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇군데에 퍼져 있는지
# 조사하면 총 몇 말이ㅢ 지렁이가 필요한지 알 수 있다.
# 예를 들어 배추 밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추 흰 지렁이가 필요하다
# 0 은 배추가 심어져 있지 않은 땅이고
# 1은 배추가 심어져 있는 땅을 나타낸낸다

import sys
from collections import deque

input = sys.stdin.readline


# BFS 함수 정의
def bfs(queue):
    print(T)
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    while queue:
        this_y, this_x = queue.popleft()
        for dy, dx in direct:
            nx, ny = this_x + dx, this_y + dy
            if 0 <= nx < M and 0 <= ny < N and matrix[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))


# 테스트 케이스 수
T = int(input())

for _ in range(T):
    # M: 가로, N: 세로, K: 배추 위치 개수
    M, N, K = map(int, input().split())

    cnt = 0

    # 배추밭과 방문 여부 초기화
    matrix = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    # 배추 위치 입력
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    # 이제 찾아야지
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1 and visited[y][x] == False:
                visited[y][x] = True
                bfs(deque([(y, x)]))
                cnt += 1
    print(cnt)

# [
# [[0, 0], [1, 0], [    ], [    ], [    ], [    ], [    ], [    ], [    ], [    ]],
# [[    ], [1, 1], [    ], [    ], [    ], [    ], [    ], [    ], [    ], [    ]],
# [[    ], [    ], [    ], [    ], [4, 2], [    ], [    ], [    ], [    ], [    ]],
# [[    ], [    ], [    ], [    ], [4, 3], [    ], [    ], [    ], [    ], [    ]],
# [[    ], [    ], [2, 4], [3, 4], [    ], [    ], [    ], [7, 4], [8, 4], [9, 4]],
# [[    ], [    ], [    ], [    ], [4, 5], [    ], [    ], [7, 5], [8, 5], [9, 5]],
# [[    ], [    ], [    ], [    ], [    ], [    ], [    ], [7, 6], [8, 6], [9, 6]],
# [[    ], [    ], [    ], [    ], [    ], [    ], [    ], [    ], [    ], [    ]]
# ]
