from sys import stdin

input = stdin.readline

N = int(input())

queue = []
for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if len(queue) != 0:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(int(len(queue) == 0))
    else:
        print((queue[0] if len(queue) != 0 else -1) if cmd[0] == "front" else queue[-1] if len(queue) != 0 else -1)
