import sys

input = sys.stdin.readline

# a : 양 한마리가 하루에먹는 사료의 양
# b : 염소 한마리가 하루에 먹는 사료의 양
# n : 양과 염소 전체의 수
# w : 하루동안 소비한 전체 사료의 양

# 양과 염소의 수

a, b, n, w = map(int, input().split(" "))

results = []

for i in range(1, n + 1):
    if i >= n:
        break
    if (a * i) + (b * (n - i)) == w:
        results.append((i, n - i))
        
print(*results[0] if len(results) == 1 else -1)