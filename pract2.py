def divident():
    x = eval(input('Please Enter number1 to devide: '))
    y = eval(input('Please Enter number2 by which you want to devide number1: '))
    if x%y == 0:
        print(str(x)+' can be devided by '+ str(y))
    else:
        print(str(x)+' can\'t be devided by '+ str(y))

divident()