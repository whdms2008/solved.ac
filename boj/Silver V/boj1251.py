from sys import stdin

string = stdin.readline()
str_list = []
for i in range(1, len(string)):
    for j in range(i + 1, len(string[i:]) + (i - 1)):
        str_list.append(string[:i][::-1] + string[i:j][::-1] + string[j:-1][::-1])
print(sorted(str_list)[0])
