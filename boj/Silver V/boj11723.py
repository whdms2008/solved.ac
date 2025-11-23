from sys import stdin

input = stdin.readline
M = int(input())
S = set()
if 1 <= M <= 3000000:
    for _ in range(M):
        cmd = input().strip().split(" ")
        S = set([i for i in range(1,21)]) if cmd[0] == "all" else set() if cmd[0] == "empty" else S
        if len(cmd) == 1:
            continue
        cmd[-1] = int(cmd[-1])
        if cmd[0] == "add":
            S.add(cmd[-1])
        elif cmd[0] == "remove":
            S.remove(cmd[-1]) if cmd[-1] in S else None
        elif cmd[0] == "check":
            print(int(cmd[-1] in S))
        elif cmd[0] == "toggle":
            S.remove(cmd[-1]) if int(cmd[-1]) in S else S.add(cmd[-1])
        elif cmd[0] == "empty":
            S = set()