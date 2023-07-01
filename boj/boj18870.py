from sys import stdin

N = int(stdin.readline())
X = list(map(int, stdin.readline().split()))

sort_X = sorted(list(set(X)))
dict_X = {sort_X[i]: i for i in range(len(sort_X))}

for i in X:
    print(dict_X[i], end=" ")
