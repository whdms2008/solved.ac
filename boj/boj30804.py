import sys
from collections import Counter

N = int(input())
S = list(map(int, input().split()))

result = 0
left = 0
counter = Counter()

for right in range(N):
    counter[S[right]] += 1

    while len(counter) > 2:
        counter[S[left]] -= 1
        if counter[S[left]] == 0:
            del counter[S[left]]
        left += 1

    result = max(result, right - left + 1)

print(result)