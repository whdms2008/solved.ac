for _ in range(int(input())):
    a = list(map(int, input().split()))
    cnt = 0
    while a[2]-a[0]>0:
        a[2] -= a[0]
        cnt += 1
    print(n*100 + r_num)
