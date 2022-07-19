import sys

n = int(sys.stdin.readline())

if 1 <= n <= 10000:
    cnt = 1
    i = 0
    while True:
        i += 1
        if "666" in str(i):
            if cnt == n:
                print(i, end="")
                break
            cnt += 1
