from sys import stdin

N, M = map(int, stdin.readline().split())

numbers = list(map(int, stdin.readline().split()))

sums = [0] * (N + 1)
for i in range(1, N + 1):
    sums[i] = sums[i - 1] + numbers[i - 1]

for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(sums[j] - sums[i - 1])
