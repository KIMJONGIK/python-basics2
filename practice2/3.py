# 3-1
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
x = s.upper()
x = re.sub('\.', '', x)
x = re.sub(',', '', x)
x = re.sub('\n', '', x)
x = x.split(' ')
x.sort()
y = []
for v in x:
    if v not in y:
        y.append(v)
print('실행 결과:')
for i in range(27):
    print(y[i])

# 3-2
import re
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
x = s.upper()
x = re.sub('\.', '', x)
x = re.sub(',', '', x)
x = re.sub('\n', '', x)
x = x.split(' ')
x.sort()
y = []
count_list = {}
for v in x:
    try:
        y.append(v)
        count_list[v] += 1
    except:
        count_list[v] = 1

print(count_list)
keyList = count_list.keys()
for word in keyList:
    print('%s : %d'%(word, count_list[word]))