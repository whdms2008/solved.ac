number_words = []

for i in range(3):
    word = input()
    if word.isdigit():
        number_words.append((i, int(word)))

number, word = max(number_words)

word += 3 - number

results = []

if word % 3 == 0 and word % 5 == 0:
    results.append("FizzBuzz")
if word % 3 == 0 and word % 5 != 0:
    results.append("Fizz")
if word % 5 == 0 and word % 3 != 0:
    results.append("Buzz")

if not results:
    print(word)
else:
    print(results[0])
