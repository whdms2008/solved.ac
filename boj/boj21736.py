"""
[ 문제 ]
대학 캠퍼스 N x M 크기이며, 상하좌우 입력한다.
만날 수 있는 사람의 수를 출력하는 프로그램 작성
"""

"""
[ 입력 ]
첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수 N(1<=N<=600), M(1<=M<600)이 주어진다
둘째 줄부터 N개의 줄에 캠퍼스 정보드링 주어진다.
O는 빈공간, X는 벽, I는 도연이, P는 사람이다.
I가 한 번만 주어짐이 보장된다.
"""

"""
[ 출력 ]
첫째 줄에는 도연이가 만날 수 있는 사람의 수를 출력한다.
단, 아무도 만나지 못한 경우 TT 를 출력한다.
"""

from collections import deque


def bfs(graph, n, m, start):
    q = deque([start])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    p_cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == "O" or graph[ny][nx] == "P":
                    if graph[ny][nx] == "P":
                        p_cnt += 1
                    q.append((nx, ny))
                    graph[ny][nx] = "X"
    return p_cnt


N, M = map(int, input().split(" "))

campus = []
do_pos = (0, 0)
for y in range(N):
    line = list(input())
    if "I" in line:
        do_pos = (line.index("I"), y)

    campus.append(list(line))

ret = bfs(campus, N, M, do_pos)

if ret:
    print(ret)
else:
    print("TT")
