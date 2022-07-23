import sys

input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if len(stack) != 0:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(int(len(stack) == 0))
    else:
        print(stack[-1] if len(stack) != 0 else -1)
