import sys

# 가변인수
print(1)
print('hello', ' ', 'world')

# sep 기본 인수값
x = 0.2
s = 'hello'
print(str(x) + ' ' + s)
print(x, s)
print(x, s, sep=' ')
print(x, s, sep=':')

# end 기본 인수값
print('hello world')
print('hello world', file = sys.stdout)
print('error:hello world', file = sys.stderr)

f = open('hello.txt', 'w')
print(type(f))
print('hello world', file = )
