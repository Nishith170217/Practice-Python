def fibonacci():
    count = eval(input('Please enter how many numbers you want to print: '))
    i = 2
    if count == 0:
        fib = []
    elif count == 1:
        fib = [0]
    elif count == 2:
        fib = [0,1]
    elif count > 2:
        fib = [0,1,1]
        while i < (count-1):
            fib.append(fib[i]+fib[i-1])
            i+=1
    return fib

print(fibonacci())