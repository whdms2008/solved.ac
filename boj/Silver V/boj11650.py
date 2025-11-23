import sys

T = int(sys.stdin.readline())
a = []
for i in range(T):
    x, y = map(int, sys.stdin.readline().strip().split(" "))
    a.append([x, y])
a.sort(key=lambda x: (x[0], x[1]))
for i in range(T):
    print(a[i][0], a[i][1])
