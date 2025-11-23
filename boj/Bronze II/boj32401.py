N = int(input())
S = input()

cnt = 0
last = 0
for s in S:
    if s == "A":
        if last == 2:
            cnt += 1
        last = 1
    if s == "N":
        if last == 1:
            last = 2
        elif last == 2:
            last = 0
print(cnt)