s = '/usr/local/bin/python'
x = s.split('/')[1:]
x = ','.join(x)
print(x)

a = s[-6:]
b = s[:-7]
c = (b, a)
c = ','.join(c)
print(c)
