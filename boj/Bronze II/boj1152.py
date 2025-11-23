a = input().split(" ")
for _ in range(a.count("")):
    a.remove("")
print(len(a))
