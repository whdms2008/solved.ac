import sys

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

lst.sort(key=lambda x: (x[1], x[0]))

result = 0
end_time = 0

for i in lst:
    if i[0] >= end_time:
        end_time = i[1]
        result += 1

print(result)
