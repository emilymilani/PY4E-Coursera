def computepay(hrs, rt):
    if hrs<=40:
        pay = hrs*rt
    else:
        pay = (40*rt) + ((hrs-40)*(1.5*rt))
    return pay

hrs = input('How many hours?')
rt = input('What is the rate?')
hrs = float(hrs)
rt = float(rt)
x = computepay(hrs, rt)
print('Pay:' , x)
