from sys import stdin  # sys 모듈에서 stdin만 사용

finds = list(map(int, stdin.readline().split()))  # stdin.readline()으로 값을 받아오고 split으

print(" ".join(str(piece - finds[i]) for i, piece in enumerate([1, 1, 2, 2, 2, 8])))
