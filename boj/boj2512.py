import sys

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())

if sum(budgets) < M:
    print(max(budgets))
else:
    left, right = 0, max(budgets)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        total_budgets = 0
        for budget in budgets:
            total_budgets += min(budget, mid)
        if total_budgets <= M:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(result)
