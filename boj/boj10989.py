import sys

T = int(sys.stdin.readline())
a = [0 for i in range(10001)]
for i in range(T):
    a[(int(sys.stdin.readline()))] += 1
for i in range(10001):
    for _ in range(a[i]):
        print(i)
