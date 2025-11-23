from sys import stdin
X = int(stdin.readline())
stick = [ 64 ]
while sum(stick) > X:
    split_stick = stick.pop(stick.index(min(stick)))
    stick.append(split_stick//2)
    if not sum(stick) >= X:
        stick.append(split_stick//2)
    for i in range(len(stick)):
        if sum(stick[i:]) == X:
            break
print(len(stick))