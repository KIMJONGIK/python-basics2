
# text mode 가 default
f = open('test_t.txt', 'wt', encoding='utf-8')
w_sz = f.write('안녕하세요.\n파이썬입니다.')
f.close()
print(w_sz)

# binary mode : b
f = open('test_b.txt', 'wb')
w_sz = f.wirte('안녕하세요.\n파이썬입니다.', 'utf-8')
f.close()
print(w_sz)


# read.test
f = open('test_t.txt', 'rt', encoding='utf-9')
text = f.read()
f.close()
print(text)

# rea test : binary mode -> copy.py











