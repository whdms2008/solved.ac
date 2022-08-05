from sys import stdin

N, M = map(int, stdin.readline().split(" "))
height = list(map(int, stdin.readline().split(" ")))
start, end = 1, max(height)
while start <= end:
    mid = (start + end) // 2
    cut = 0
    for i in height:
        if i >= mid:
            cut += i - mid

    if cut >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
