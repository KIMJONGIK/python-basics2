l = (10, 12, 14, 15, 17, 18, 19, 20, 25, 30, 32, 33, 37, 40, 42, 44, 46, 50)
count = 0
sum = 0
for number in l:
    a = number//10          # 손으로 3의 배수를 구할 때 쓰는 방법 : 각 자리수의 합이 3의 배수인가 판별
    b = number - a*10
    if (a+b) % 3 == 0:
        count += 1
        sum += number
print('주어진 리스트에서 3의 배수의 개수=> %d'%count)
print('주어진 리스트에서 3의 배수의 합=> %d'%sum)