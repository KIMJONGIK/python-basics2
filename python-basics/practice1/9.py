menu = {'오뎅':300, '순대':400, '만두':500}
menu_input = input('메뉴: ')
price = menu[menu_input]
print('가격: ' + format(price, 'd'))