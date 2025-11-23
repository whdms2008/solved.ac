from sys import stdin
from math import ceil

A, B, V = list(map(int, stdin.readline().split(" ")))

print(ceil((V-B)/(A-B)))