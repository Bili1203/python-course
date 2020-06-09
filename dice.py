import random

print ('DICE ROLL SIMULATOR')
print ('-------------------')

while True:
    wanna = input ('Wanna roll? (y/n) ')
    if wanna== 'y':
        print ('You have rolled :', random.randint(1,6))
    elif wanna == 'n':
        break
    else:
        continue

print ('Bye!')