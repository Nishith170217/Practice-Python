def rockG():
    p1= input('Dear P1; please enter rock or paper or scissors :')
    p2= input('Dear P2; please enter rock or paper or scissors :')

    if p1==p2:
        print('Its a tie..')
    elif p1=='rock':
        if p2=='scissors':
            print('P1 wins..')
        else:
            print('P2 Wins')
    elif p1=='paper':
        if p2=='scissors':
            print('p2 wins...')
        else:
            print('p1 wins...')
    elif p1== 'scissors':
        if p2=='rock':
            print('P2 wins...')
        else:
            print('p1 Wins...')

rockG()