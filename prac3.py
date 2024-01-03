def chosenlist(ol):
    new_list=[]
    for element in ol:
        if element <= 5:
            new_list.append(element)
    print(new_list)

ol= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
chosenlist(ol)