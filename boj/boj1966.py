from sys import stdin

T = int(stdin.readline())

for i in range(T):
    N, M = map(int, stdin.readline().split())
    a = [i for i in range(1, N + 1)]
    b = list(map(int, stdin.readline().split()))
    chk = a[M]
    cnt = 0
    while len(a) != 0:
        if b.index(max(b)) != 0:
            for j in range(b.index(max(b))):
                a.append(a[0])
                b.append(b[0])
                del a[0], b[0]
        else:
            cnt += 1
            if chk == a[0]:
                break
            del a[0], b[0]
    print(cnt)
