a = 0
b = []
for i in range(9):
    b.append(int(input()))
    if b[a] < b[i]:
        a = i
print(b[a])
print(a + 1)
