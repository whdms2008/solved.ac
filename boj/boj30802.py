N = int(input())
sizes = map(int, input().split(" "))
T, P = map(int, input().split(" "))

print(f"{sum([(size // T) + (1 if (size % T) else 0) for size in sizes])}\n{N // P} {N % P}")