import sys

T = int(sys.stdin.readline())
a = set([])
for i in range(T):
    data = sys.stdin.readline().strip()
    a.add(data)
a = list(a)
a.sort()
a.sort(key=len)
for i in a:
    print(i)
