arr = []
i = int(input('i = '))
for i in range(int(input('n = '))):
    arr.append(int(input(f'a[{i}] = ')))
arr.pop(i)
for i in arr:
    print(i, end = ' ')