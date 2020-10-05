out = 'y'
while out == 'y':
    x = input('수를 입력하세요: ')
    if int(x) % 2 == 1:
        print('홀수')
    else:
        print('짝수')
    out = input('계속 하시겠습니까? y/n : ')
