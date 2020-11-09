hrs = input('How many hours?')
rt = input('What is the rate?')
hrs = float(hrs)
rt = float(rt)

if hrs<=40:
    pay = hrs*rt
else:
    pay = (40*rt) + ((hrs-40)*(1.5*rt))
print('Pay:' , pay)
