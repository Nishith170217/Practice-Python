def binarySearch(s,l):
    low = 0
    high = len(l)-1
    

    while low <= high:
        mid = (high+low)//2
        guess = l[mid]
        if guess == s:
            return mid
        elif guess > s:
            high = mid - 1
        else:
            low = mid + 1
        
    return None

a = [1, 3, 5, 30, 42, 43, 500]
n = 43

print(binarySearch(n,a))




