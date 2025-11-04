import sys

N, M = map(int, sys.stdin.readline().split())
min_pack = 10**9
min_single = 10**9

for _ in range(M):
    p, s = map(int, sys.stdin.readline().split())
    if p < min_pack:
        min_pack = p
    if s < min_single:
        min_single = s

ans = min(
    N * min_single, (N // 6) * min_pack + (N % 6) * min_single,  ((N + 5) // 6) * min_pack
)
print(ans)
