text = "X-DSPAM-Confidence:    0.8475"
numpos = text.find('0')
num = text[numpos : numpos+6]
num = float(num)
print(num)
