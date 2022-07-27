from sys import stdin

N, M = list(map(int,stdin.readline().split(" ")))
height = list(map(int,stdin.readline().split(" ")))
a = list(range(N))
start = min(height)
end = max(height)
while start <= end:
    mid_cut = (start + end) // 2
    a = sum([height[i]-mid_cut if height[i]-mid_cut > 0 else 0 for i in range(N)])
    if a == M:
        print(mid_cut)
        break
    elif a > M:
        start = mid_cut + 1
    else:
        end = mid_cut -1