import sys

def factorial(n):
    if(n > 1):
        return n * factorial(n - 1)
    else:
        return 1

a = int(sys.stdin.readline())
print(factorial(a))