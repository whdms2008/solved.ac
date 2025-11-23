from sys import stdin


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


cnt = 0
for i in str(factorial(int(stdin.readline())))[::-1]:
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)
