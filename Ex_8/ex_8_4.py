file = open('romeo.txt')
words_ls = list()
for line in file:
    line_words = line.split()
    for word in line_words:
        if word not in words_ls:
            words_ls.append(word)
words_ls.sort()
print(words_ls)