from sys import stdin

N, M = list(map(int,stdin.readline().split(" ")))
height = list(map(int,stdin.readline().split(" ")))
a = list(range(N))
mid_cut = max(height) // 2
while True:
    a = sum([height[i]-mid_cut if height[i]-mid_cut > 0 else 0 for i in range(N)])
    print(mid_cut, a)
    if a == M:
        print(mid_cut)
        break
    mid_cut += 1 if a > M else -1