A = sum(map(int, [int(input()) * i for i in range(3, 0, -1)]))
B = sum(map(int, [int(input()) * i for i in range(3, 0, -1)]))

print("A" if A > B else "B" if B > A else "T")