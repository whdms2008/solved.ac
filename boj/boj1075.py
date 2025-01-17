N = int(input()[:-2] + "00")
F = int(input())

for num in range(100):
    if N % F == 0:
        print(f"{num:02}")
        break
    N += 1
