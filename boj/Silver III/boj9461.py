from sys import stdin

P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    if N >= len(P):
        for i in range(len(P), N):
            P.append(P[i-2] + P[i-3])
    print(P[N-1])

