from sys import stdin, setrecursionlimit
setrecursionlimit(10000)


def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)


n, m = map(int, stdin.readline().split())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

for v in range(1, n + 1):
    if not visited[v]:
        dfs(v)
        cnt += 1

print(cnt)
