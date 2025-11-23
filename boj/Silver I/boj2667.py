# 단지번호붙이기

"""
[ 문제 ]
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타냄
이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 함
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래 위로 다른 집이 있는경우를 말한다.

대각선상에 집이 있는 경우는 연결된 것이 아니다.

지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를
오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""

"""
[ 입력 ]
첫번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5<=N<=25)
이 입력되고, 그 다음은 N줄에 각각 N개의 자료(0혹은 1)가 입력된다.
"""

"""
[ 출력 ]
첫 번째 줄에는 총 단지수를 출력하시오, 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력 하시오,
"""

from collections import deque

def bfs(graph, n):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    danzis = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                q = deque([(j, i)])
                zips = [(j,i)]
                while q:
                    x, y = q.popleft()
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if (nx, ny) in zips:
                            continue
                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[ny][nx] == 1:
                                zips.append((nx, ny))
                                q.append((nx, ny))
                for nx, ny in zips:
                    graph[ny][nx] = 0
                danzis.append(len(zips))
    return danzis


N = int(input())

matrix = [list(map(int, " ".join(input()).split(" "))) for _ in range(N)]

danzis = sorted(bfs(matrix, N))
print(len(danzis))
for num in danzis:
    print(num)
