# 케빈 베이컨의 6단계 법칙에 의하면 지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있다.
# 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임이다.

# 예를 들면, 전혀 상관없을 것 같은 인하대학교의 이강호와 서강대학교의 민세희는 몇 단계만에 이어질 수 있을까?

# 천민호는 이강호와 같은 학교에 다니는 사이이다.
# 5명
# [1 : {3, 4}, 2 : { 3 }, 3 : { 4 }, 4 : { 5 }


# 1 :

#

import sys
from collections import defaultdict, deque


def bfs(start, target):
    queue = deque([start])
    cnt = 0
    while queue:
        number = queue.popleft()
        cnt += 1
        for item in graph[number]:
            print(f"start : {start}, item: {item}, target: {target}, cnt: {cnt}")
            if item == target:
                steps[start - 1][target - 1] = cnt
                steps[target - 1][start - 1] = cnt
                return
            if not visited[item - 1]:
                visited[item - 1] = True
                queue.append(item)

# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# defaultdict(<class 'list'>, {1: [3, 4], 3: [1, 4, 2], 4: [1, 5, 3], 5: [4], 2: [3]})



input = sys.stdin.readline

N, M = map(int, input().split(" "))

graph = defaultdict(list)
visited = [False for _ in range(N + 1)]
steps = [[0] * N for _ in range(N)]

for _ in range(N):
    A, B = map(int, input().split(" "))
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if not visited[i - 1]:
            visited[i - 1] = True
        bfs(i, j)


print(graph)

