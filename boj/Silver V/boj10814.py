import sys

T = int(sys.stdin.readline())
a = []
for i in range(T):
    year, name = sys.stdin.readline().strip().split(" ")
    a.append([i, int(year), name])
a.sort(key=lambda x: (x[1], x[0]))
for i in range(T):
    print(a[i][1], a[i][2])
