dobry = 0
zły = 0
ostatni = ''

linia = input()
while linia != '':
    if linia == 'злой':
        zły += 1
        ostatni = 'злой'
    elif linia == 'добрый':
        dobry += 1
        ostatni = 'добрый'
    elif linia == 'Какой подарок?':
        if ostatni == 'добрый' and dobry > zły:
            print('серебряный шиллинг')
        elif ostatni == 'злой' and zły > dobry:
            print('золотой')
        else:
            print('Ах, не знаю!')
            break
        
        dobry = 0
        zły = 0
        ostatni = ''

    linia = input()