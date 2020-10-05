change = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 50, 1]

a = int(input('금액 : '))

for money in change:
    count = a//money
    a = a - count * money
    print(f'{money} : {count}개')
