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
