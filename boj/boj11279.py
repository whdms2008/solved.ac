from sys import stdin
from heapq import heappush, heappop

heap = []
for i in range(int(stdin.readline())):
    num = int(stdin.readline())
    if not num:
        print(0 if not heap else heappop(heap)[1])
    else:
        heappush(heap, (-num, num))
