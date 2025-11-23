import sys
cnt = int(sys.stdin.readline())
for i in range(cnt):
    try:
        a, b = map(int, sys.stdin.readline().split())
    except:
        break
    print(a + b)
