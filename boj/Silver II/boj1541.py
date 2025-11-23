from sys import stdin

logic = stdin.readline().strip()
parts = logic.split("-")
for i in range(len(parts)):
    if "+" in parts[i]:
        parts[i] = "+".join(list(map(str, list(map(int, parts[i].split("+"))))))
    else:
        parts[i] = str(int(parts[i]))

best = [eval(part) for part in parts]
min_value = best[0] - sum(best[1:])

print(min_value)
