from sys import stdin

while True:
    N = stdin.readline()
    if N.strip() == "." and len(N) == 2:
        break
    chk = ""
    for i in N:
        if i == "(" or i == "[":
            chk +=i
        if i == ")" or i == "]":
            chk +=i
    for i in range(len(chk) // 2):
        chk = chk.replace("()", "")
        chk = chk.replace("[]", "")
    print("yes") if chk == "" else print("no")
