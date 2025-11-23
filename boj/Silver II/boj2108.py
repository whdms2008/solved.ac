from sys import stdin
from collections import Counter

input = stdin.readline

N = int(input())

data = sorted([int(input()) for i in range(N)])
print(round(sum(data)/N))
idx = len(data)//2
if len(data) % 2 == 0:
    print(round((data[idx-1] + data[idx]) / 2))
else:
    print(data[idx])
min_value = Counter(data)
for i in list(min_value.keys()):
    if max(min_value.values()) > min_value[i]:
        min_value.pop(i)
if len(min_value) >= 2:
    min_value.pop(min(min_value))
print(min(min_value))
print(abs(min(data) - max(data)))
