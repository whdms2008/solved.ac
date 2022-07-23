from sys import stdin

input = stdin.readline

N = int(input())

deque = []
for _ in range(N):
    cmd = input().strip().split("_")
    if cmd[0] == "push":
        deque.append(int(cmd[1][5:])) if cmd[1][:4] == "back" else deque.insert(0, int(cmd[1][6:]))
    elif cmd[0] == "pop":
        print((deque.pop(0) if len(deque) != 0 else -1) if cmd[1] == "front" else (
            deque.pop(-1) if len(deque) != 0 else -1))
    elif cmd[0] == "size":
        print(len(deque))
    elif cmd[0] == "empty":
        print(int(len(deque) == 0))
    else:
        print((deque[0] if len(deque) != 0 else -1) if cmd[0] == "front" else deque[-1] if len(deque) != 0 else -1)
