import sys

cnt, max = map(int, sys.stdin.readline().split())
for i in range(cnt):
    try:
        x = list(map(int, sys.stdin.readline().split()))
        for i in x:
            if i < max:
                print(i)
    except:
        break
