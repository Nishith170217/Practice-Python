import random

x = random.randint(1,9)
c = 0
y = 0
while(x!=int(y) or y=='exit'):

    y = input('Please enter a number: ')
    if y == 'exit':
        break
    elif x==y:
        print('Great! Your guess is right')
        break
    else:
        c+=1
        print('Wrong !!! Try Again! ')
        continue

print('You tried for '+str(c)+' times.')
