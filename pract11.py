def primefinder():
    flag = 0
    inp = eval(input('Please Enter a number to check prime: '))
    if inp==1:
         #print('The number is not prime.')
         flag = 1
    else:
        for i in range(2,inp):
            if inp%i == 0:
                #print('The number is not prime. ')
                flag = 1
                break
            
            else:
                flag=5
                #print('The number is prime. ')
            

    if flag==1:
        print('The number is not prime. ')
    else:
        print('The number is prime. ')      


primefinder()