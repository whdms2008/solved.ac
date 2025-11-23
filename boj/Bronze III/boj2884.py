a, b = list(map(int, input().split()))
c = b-45
if c < 0:
    b = c+60
    if a == 0:
        a = 23
    else:
        a -= 1
else:
    b = c
print(a, b)