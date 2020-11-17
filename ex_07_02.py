count = 0
total = 0

uinp = input('Enter file name: ')
fhand = open(uinp)
for aline in fhand:
    if aline.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        bline = aline.find(':')
        cline = aline[bline + 1:]
        dline = float(cline)
        total = total + dline
average = total / count
print('Average spam confidence:' , average)
