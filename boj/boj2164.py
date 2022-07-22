import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([i for i in range(1, N+1)])

while True:
    print(q)
    q.popleft()
    q.reverse()