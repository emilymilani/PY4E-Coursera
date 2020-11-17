file = input('Enter file name: ')
fhand = open(file)
for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)
