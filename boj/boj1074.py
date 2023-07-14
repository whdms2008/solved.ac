from sys import stdin

N, r, c = map(int, stdin.readline().split())


def recur(N, r, c):
    return 2 * (r % 2) + (c % 2) + 4 * recur(N - 1, r // 2, c // 2) if N else 0


print(recur(N, r, c))
