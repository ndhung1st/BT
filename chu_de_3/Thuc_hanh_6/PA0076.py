s1 = input('sau 1: ')
s2 = input('sau 2: ')
s1p = ''
for i in range(-1, -len(s1) - 1, -1):
    s1p += s1[i]
if s1p == s2:
    print("YES")
else:
    print('NO')
