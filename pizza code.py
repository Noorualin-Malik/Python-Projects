pizza=input('which pizza do you want(s,m,l)?')
bill=0
if pizza=='s':
    print('you have to pay 100 Rs.')
    bill=100
    pepperoni=input('do you want extra pepperoni?')
    if pepperoni=='y':
        print('you have to pay extra 30 Rs.')
        bill+=30
    else:
        print(f'you have to pay {bill}')
    cheese=input('do you want extra cheeze?')
    if cheese=='y':
      print('you have to pay extra 20 Rs.')
      bill+=20
    else:
        print(f'you have to pay {bill}')
else:
    print(f'you have to pay {bill}')
if pizza=='m':
    print('you have to pay 200 Rs.')
    bill=200
    pepperoni=input('do you want extra pepperoni?')
    if pepperoni=='y':
        print('you have to pay extra 50 Rs.')
        bill+=50
    else:
        print(f'you have to pay {bill}')
    cheese=input('do you want extra cheeze?')
    if cheese=='y':
      print('you have to pay extra 20 Rs.')
      bill+=20
    else:
        print(f'you have to pay {bill}')
else:
    print(f'you have to pay {bill}')
if pizza=='l':
    print('you have to pay 300 Rs.')
    bill=300
    cheese=input('do you want extra cheeze?')
    if cheese=='y':
      print('you have to pay extra 20 Rs.')
      bill+=20
    else:
        print(f'you have to pay {bill}')
else:
    print(f'you have to pay{bill}')




