def reverse(x):
    #teststr = 'My name is Nishith'
    sp = x.split() 
    sp.reverse()
    sp = ' '.join(sp)
    return sp

x = input('Please enter a string to reverse the order: ')
print(reverse(x))