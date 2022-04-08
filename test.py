f = open('users.txt', 'r')
text1 = f.read()
txt1 = text1.split(',')
have1 = 0
print(txt1)
for i in txt1:
    if i == 'Alishernumonov':
        have1 = 1
f.close()
if have1 == 0:
    f = open('users.txt', 'a')
    f.write(f'o\'xshamadi,')
    f.close()
print(have1)
a = input()
