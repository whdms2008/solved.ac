import sys

T = int(sys.stdin.readline())
for _ in range(T):
    f = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    bee = list(range(1, n + 1))
    for j in range(f):
        aff = []
        for k in range(1, n + 1):
            aff.append(0)
            aff[k - 1] = sum(bee[:k])
        bee = aff
    print(bee[n - 1])
