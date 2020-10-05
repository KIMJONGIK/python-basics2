def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

a = input("수를 입력하세요 : ")
if a.isdigit() == True:
    if int(a) % 3 == 0:
        print('3의 배수입니다.')
    elif int(a) % 3 == 1:
        print('3의 배수가 아닙니다.')
    else:
        print('3의 배수가 아닙니다.')
else:
    print('정수가 아닙니다.')

