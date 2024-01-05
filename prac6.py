def rev(string1):
    newstr = ''
    for i in range (len(string1)-1,-1,-1):
        newstr+= string1[i]
    
    return newstr

string = input('Please Enter a string : ')

if string == rev(string):
    print('This string is palindrome')
else:
    print('This string is not palindrome')
