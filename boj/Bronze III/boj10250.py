for _ in range(int(input())):
    a = list(map(int, input().split()))
    cnt = 1
    while a[2]-a[0]>0:
        a[2] -= a[0]
        cnt += 1
    print(a[2]*100 + cnt)
