a = input('숫자를 입력하세요 : ')
a = int(a)
if a % 2 == 1:
    k = (a - 1) / 2
    print(f'결과 값 : {int(k * (k + 1) + k + 1)}') # 홀수합 일반항
else:
    k = a / 2
    print(f"결과 값 : {int(k * (k + 1))}") # 짝수합 일반항