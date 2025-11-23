
a = list(map(int, input().split()))
b = 0
for i in a:
    b += i**2
print(b % 10)