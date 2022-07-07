a = int(input())
a *= int(input())
a *= int(input())
b = list(map(int, str(a)))
for i in range(10):
    print(b.count(i))
