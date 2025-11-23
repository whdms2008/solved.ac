N, M = map(int, input().split())
min_package, min_pcs = 10 ** 3, 10 ** 3
for _ in range(int(M)):
    package, pcs = map(int, input().split())
    if min_package > package:
        min_package = package
    if min_pcs > pcs:
        min_pcs = pcs

print(min(
    N * min_pcs, (N // 6) * min_package + (N % 6) * min_pcs, ((N + 5) // 6) * min_package
))
