import sys

scores = list(map(int, input().split(" ")))

Bob = sum(scores)/20
index_20 = scores.index(20)
Alice = (scores[index_20-1] + scores[index_20] + scores[(index_20 + 1) % 20]) / 3
print("Bob" if Bob > Alice else "Alice" if Bob < Alice else "Tie")
