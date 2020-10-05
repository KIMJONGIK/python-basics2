import re
subjs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

sentece = [(s, v, o) for s in subjs for v in verbs for o in objs]
for i in sentece:
    a = ','.join(i)
    a = a.replace(',', ' ')
    print(a)