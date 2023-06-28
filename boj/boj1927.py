from sys import stdin
import heapq

heap = []
for _ in range(int(stdin.readline())):
    x = int(stdin.readline())
    if x:
        heapq.heappush(heap, x)
    else:
        print(heapq.heappop(heap) if len(heap) else 0)
