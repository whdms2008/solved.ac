X = int(input().split()[1])
print(*[n for n in map(int, input().split()) if X > n])
