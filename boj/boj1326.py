import sys
from collections import deque


def bfs(graph, start_node, end_node, n):
    q = deque([start_node])
    dx = [1, -1]
    for i in range(n):
        for idx in range(2):
            nx = start_node + dx[idx] # 1
            # 2 = 1 + 1 [ 우측 으로 이동했을때? ]
            if 0 <= nx < n:
                q.append(nx)
        while q:
            x = q.popleft()



N = int(input())
stones = list(map(int, input().split(" ")))

print(bfs(stones, N))
