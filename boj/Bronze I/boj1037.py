if int(input()) == 1:
    print(int(input()) ** 2)
    exit(0)

N_list = sorted(list(map(int, input().split(" "))))
print(max(N_list) * min(N_list))
