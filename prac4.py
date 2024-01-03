def divisors():
    l= []
    num = eval(input('please enter a number: '))

    for i in range(2,num-1):
        if num % i == 0:
            l.append(i)
    print(l)

divisors()