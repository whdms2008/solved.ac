a = int(input())
b = 0
for i in range(1, a+1):
    c = 0
    c += i + sum(list(map(int,str(i))))
    if c == a:
        b = i
        break
print(b)


