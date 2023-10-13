from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

queue = deque()

maze = [stdin.readline().strip() for _ in range(N)]

n = 2
m = 2
cnt = 0
while True:
    cnt += 1
    if 0 < n - 1 < N:
        queue.append(maze[n - 1][m])
    if 0 < m - 1 < M:
        queue.append(maze[n][m - 1])
    if n + 1 < N:
        queue.append(maze[n + 1][m])
    if m + 1 < M:
        queue.append(maze[n][m + 1])
    print(queue)
    n += 1
    m += 1
    for i in queue:
        print(i)
    print(queue)
    if cnt == 1:
        break
