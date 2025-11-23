from sys import stdin

N, M = map(int, stdin.readline().split(" "))
site = {}
for _ in range(N):
    url, pwd = stdin.readline().strip().split(" ")
    site[url] = pwd

for _ in range(M):
    print(site[stdin.readline().strip()])