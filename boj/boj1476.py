from sys import stdin

E, S, M = list(map(int, stdin.readline().split()))

M_e = 15
M_s = 28
M_m = 19

i, j, k = 0, 0, 0
year = 0
while True:
    if i == E and j == S and k == M:
        break
    year += 1
    i += 1 if i < M_e else - (M_e - 1)
    j += 1 if j < M_s else - (M_s - 1)
    k += 1 if k < M_m else - (M_m - 1)
print(year)
