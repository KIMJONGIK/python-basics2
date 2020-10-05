import random
gugu = [(i*j)  for i in range(2, 10) for j in range(1, 10)]
dan = []
for i in range(2, 10):
    for j in range(1, 10):
        dan.append(f'{i} X {j}')

gugudan = {}
for i in range(0, 72):
    gugudan[dan[i]] = gugu[i]

sample = random.sample(dan, 9)
ans = random.choice(sample)
ans_f = ans
sample = [gugudan[i] for i in sample]
ans_f = gugudan[ans_f]

print(f'{ans} = ?')

p = [0, 3, 6]
for i in p:
    for j in range(0, 3):
        print(f'{sample[i+j]}', end='\t')
        j += 1
    print('\n')

a = int(input('answer : '))
if a == ans_f:
    print('정답')
else:
    print('오답')

