smallest = None
largest = None

while True:
    numb = input('Enter number: ')
    if numb == 'Done':
        break
    try:
        numb=int(numb)
    except:
        print('Invalid input')
        continue

    if smallest is None:
        smallest = numb
    elif numb < smallest:
        smallest = numb
    if largest is None:
        largest = numb
    elif numb > largest:
        largest = numb


print('Maximum is' , largest)
print('Minimum is' , smallest)
