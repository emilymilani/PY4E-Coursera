score = input('Score:')
score = float(score)

if score<0:
    print('Invalid score')
    quit()
elif score>1:
    print('Invalid score')
    quit()
elif score>=.9:
    print('A')
elif score>=.8:
    print('B')
elif score>=.7:
    print('C')
elif score>=.6:
    print('D')
else:
    print('F')
