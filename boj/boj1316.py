T = int(input())

list_cnt = 0
for _ in range(T):
    words = input()
    set_word = []
    list_cnt += 1
    for word in words:
        if word in set_word:
            if set_word[-1] == word:
                continue
            else:
                list_cnt -= 1
                break
        else:
            set_word.append(word)
print(list_cnt)
