total = 0
count = 0

while True:
    number = input('Enter number:')
    if number == 'Done':
        break
    try:
        number = float(number)
    except:
        print('Invalid number')
        continue

    total = total + number
    count = count + 1

print(total, count, total/count)
