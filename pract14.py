def list_d1(l):
    new = []
    for x in l:
        if x not in new:
            new.append(x)
    return new

#using set
def list_d2(a):
    s = set(a)
    return list(s)

a = [1,2,3,4,3,2,1]

print(a)
print(list_d1(a))
print(list_d2(a))
