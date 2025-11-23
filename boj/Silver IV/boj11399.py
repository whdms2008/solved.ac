from sys import stdin

N = int(stdin.readline())

time = list(map(int, stdin.readline().split(" ")))
time.sort()
total = 0
for i in range(N):
    total += sum(time[:i], time[i])
print(total)
