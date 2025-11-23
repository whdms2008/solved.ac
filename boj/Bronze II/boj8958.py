T = int(input())
for _ in range(T):
    score = 0
    chk = 0
    a = input()
    for i in range(len(a)):
        if a[i] == "O":
            score += 1 + chk
            chk += 1
        else:
            chk = 0
    print(score)
