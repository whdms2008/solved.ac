from sys import stdin
from collections import deque

N, K = list(map(int, stdin.readline().split()))


def bfs(N, K):
    MAX = 100001
    queue = deque([(N, 0)])
    visited = [0] * MAX

    while queue:
        v, t = queue.popleft()

        if v == K:
            return t

        for next_v in [v - 1, v + 1, v * 2]:
            if 0 <= next_v < MAX and not visited[next_v]:
                visited[next_v] = 1
                queue.append((next_v, t + 1))
    return None


print(bfs(N, K))
