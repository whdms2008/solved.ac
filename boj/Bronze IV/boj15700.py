N, M = map(int, input().split(" "))

A, B = 0, 0
if N >= 2 and M >= 1:
    A = (N // 2) * (M // 1)
    N -= 2 * (N // 2)
if N >= 1 and M >= 2:
    B = (N // 1) * (M // 2)
print(A+B)