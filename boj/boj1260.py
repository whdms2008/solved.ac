from sys import stdin
from collections import deque, defaultdict


def Search(type, t, vt):
    d = deque()
    d.append(vt)
    v, r = {vt}, [vt]
    while d:
        if vt in t:
            d += t[vt] if type == "bfs" else reversed(t[vt])
        while d:
            vt = d.pop() if type == "dfs" else d.popleft()
            if vt not in v:
                v.add(vt)
                r.append(vt)
                break
    return r


N, M, V = map(int, stdin.readline().split())

tree = defaultdict(list)

for _ in range(M):
    num1, num2 = map(int, stdin.readline().split())
    tree[num1].append(num2)
    tree[num2].append(num1)

for adj in tree.values():
    adj.sort()

print(" ".join(map(str, Search("dfs", tree, V))))
print(" ".join(map(str, Search("bfs", tree, V))))
