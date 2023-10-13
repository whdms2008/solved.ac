from sys import stdin

string = list(stdin.readline().strip()) ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
M = int(stdin.readline())
cur = len(string) - 1
for _ in range(M):
    command = stdin.readline().replace(" ", "")
    match command[0]:
        case "P":
            string.insert(cur + 1 if cur != 0 else 0, command[1])
            cur += 1
        case "L":
            cur -= 1 if cur > 0 else 0
        case "D":
            cur += 1 if cur < len(string) - 1 else 0
        case "B":
            if cur != 0:
                cur -= 1 if cur >= len(string) - 1 else 0
                string.pop(cur)

for i in string:
    print(i, end="")
