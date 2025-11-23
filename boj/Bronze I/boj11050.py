import sys
import math

n, k = map(int,sys.stdin.readline().split(" "))
print(int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k))))