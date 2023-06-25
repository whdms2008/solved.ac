from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    costume = {}
    for _ in range(int(stdin.readline())):
        value, key = stdin.readline().split(" ")
        if key in costume:
            costume[key] += 1
        else:
            costume[key] = 1

    result = 1
    for cnt in costume.values():
        result *= (cnt + 1)

    print(result-1)
