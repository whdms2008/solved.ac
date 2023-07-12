from sys import stdin

N = int(stdin.readline())
text = stdin.readline()

for i in range(N-1):
    for j, word in enumerate(stdin.readline()):
        if text[j] != word:
            text = text[:j] + "?" + text[j+1:]
print(text)
