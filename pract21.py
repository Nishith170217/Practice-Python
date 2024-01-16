def drawboard(col):
    col = int(col)
    i = 0
    ho = "--- "
    ve = "|   "
    ho = ho * col
    ve = ve * (col+1)
    while i < col+1:
        print(ho)
        if not (i == col):
            print(ve)
        i += 1

col = input('Enter column: ')
drawboard(col)