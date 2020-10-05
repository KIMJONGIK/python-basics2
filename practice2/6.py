import random
rng_min = 1
rng_max = 100

ans = random.randint(1, 100)
print(ans)
number = int(input('수를 결정하였습니다. 맞추어 보세요. \n1-100'))

while True:
    if number == ans:
        print('맞았습니다.')
        key = input('다시 하시겠습니까(y/n)')
        if key == 'n':
            break
        else:
            ans = random.randint(1, 100)
            print(ans)
            number = int(input('수를 결정하였습니다. 맞추어 보세요. \n1-100'))

    elif number < ans:
        rng_min = number
        print(rng_min, '-', rng_max)
        number = int(input('더 높게'))

    elif number > ans:
        rng_max = number
        print(rng_min, '-', rng_max)
        number = int(input('더 낮게'))
