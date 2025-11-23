import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
c_N = list(map(int,input().split(" ")))
M = int(input())
c_M = list(map(int,input().split(" ")))

a = Counter(c_N)

for i in range(M):
    print(a[c_M[i]], end = " ")