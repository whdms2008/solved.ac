a = input().upper()
a_b = list(set(a))
value = []
for i in range(len(a_b)):
    value.append(a.count(a_b[i]))
if value.count(max(value)) == 1:
    print(a_b[value.index(max(value))])
else:
    print("?")
