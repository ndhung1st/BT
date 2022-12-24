n = int(input('n = '))
v = int(input('v = '))
arr = []
i = 1
while i <= n:
    arr.append(int(input(f'a[{i}] = ')))
    i += 1
j = 1
for i in arr:
    if i == v:
        print("YES")
        print(j)
        j = True
        break
    j += 1
if j != True:
    print("NO")