from sys import stdin

N = int(stdin.readline())

lst = list(map(int, stdin.readline().split()))
lst2 = [ i for i in range(1, len(lst)+1)]
print(lst)

for i in range(1, N+1):
    print(f"{i} 보다 큰 수 - {[i for i in range(i+1 , i+lst[i-1]+1)]}")
    if lst[i-1] == len(lst2[:lst2.index(i)]):
        continue
    else:
        

