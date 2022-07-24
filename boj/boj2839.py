from sys import stdin

N = int(stdin.readline())

a = N // 5
cnt = 0
check = []
for i in range(1, a + 1):
    if ((N - (5 * i)) % 3) == 0:
        check.append(i)
if len(check) != 0:
    cnt = max(check)
N -= 5 * cnt
if N % 3 == 0:
    cnt += N // 3
if cnt == 0:
    cnt = -1
print(cnt)
