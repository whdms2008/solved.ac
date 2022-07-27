from sys import stdin

K, N = map(int, stdin.readline().split(" "))
data = [int(stdin.readline()) for _ in range(K)]
start = 1
end = max(data)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    if sum(data[i] // mid for i in range(K)) >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
