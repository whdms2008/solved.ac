import sys

T = int(sys.stdin.readline())
a = []
for i in range(T):
    a.append(int(sys.stdin.readline()))
a.sort()
for i in range(T):
    print(a[i])