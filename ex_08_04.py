words = list()
fhand = open('romeo.txt')
for line in fhand:
    aline = line.split()
    for w in aline:
        if w not in words:
            words.append(w)
words.sort()
print(words)
