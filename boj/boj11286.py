import sys
import heapq

input = sys.stdin.readline

hq = []

N = int(input())

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
        continue
    heapq.heappush(hq, (abs(num), num))
