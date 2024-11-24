# 미키의 뒷마당에는 특정 수의 양이 있다. 그가 푹 잠든 사이에 배고픈 늑대는 마당에 들어와 양을 공격했다.
#
# 마당은 행과 열로 이루어진 직사각형 모양이다. 글자 '.' (점)은 빈 필드를 의미하며,
# 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다.
#
# 한 칸에서 수평, 수직만으로 이동하며 울타리를 지나지 않고 다른 칸으로 이동할 수 있다면,
# 두 칸은 같은 영역 안에 속해 있다고 한다. 마당에서 "탈출"할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주한다.
#
# 다행히 우리의 양은 늑대에게 싸움을 걸 수 있고 영역 안의 양의 수가 늑대의 수보다 많다면 이기고,
# 늑대를 우리에서 쫓아낸다. 그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다.
#
# 맨 처음 모든 양과 늑대는 마당 안 영역에 존재한다.
#
# 아침이 도달했을 때 살아남은 양과 늑대의 수를 출력하는 프로그램을 작성하라.

import sys

input = sys.stdin.readline

R, C = map(int, input().split(" "))

# 조건,
# . = 0
# o = 1
# v = 2

# matrix[y][x] 가 o 또는 v 일때
# 상하좌우로 이동하며, 이동 가능한 칸 .(0) 으로 이동하며, 더이상 이동할 수 없을때까지 이동한다.
# 마당 밖에 있는 경우는 없다.
# 무조건 울타리 안에만 있음
from collections import deque

def BFS(queue):
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sheep_cnt = 0
    wolf_cnt = 0
    while queue:
        y, x = queue.popleft()
        if matrix[y][x] == "o":
            sheep_cnt += 1
        elif matrix[y][x] == "v":
            wolf_cnt += 1
        for dy, dx in direct:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx] and matrix[ny][nx] != "#" :
                queue.append((ny, nx))
                visited[ny][nx] = True

    return sheep_cnt, wolf_cnt

matrix = [input().rstrip() for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

result = [0, 0]
for i in range(R):
    for j in range(C):
        if (matrix[i][j] == "o" or matrix[i][j] == "v") and not visited[i][j]:
            visited[i][j] = True
            sheep, wolf = BFS(deque([(i, j)]))
            if sheep <= wolf:
                result[1] += wolf
            else:
                result[0] += sheep
print(*result)
