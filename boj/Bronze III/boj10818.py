T = int(input())
a = list(map(int, input().split(" ")))
a_min = 1000000
a_max = -1000000
for i in range(T):
    if a[i] <= a_min:
        a_min = a[i]
    if a[i] >= a_max:
        a_max = a[i]
print(a_min, a_max, end="")
