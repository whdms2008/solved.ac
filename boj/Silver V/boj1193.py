import sys

input = sys.stdin.readline

X = int(input())

if X == 1:
    print("1/1")
else:
    chk = False
    result = 1
    for num in range(2, X + 1):
        result += num
        y, x = (1, num) if chk else (num, 1)
        chk = not chk

        if result >= X:
            abs_result = abs(result - X)
            x = x + abs_result if y != 1 else x - abs_result
            y = y - abs_result if y != 1 else y + abs_result
            print(f"{y}/{x}")
            break
