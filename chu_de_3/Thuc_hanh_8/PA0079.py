a = [1,1]
n = int(input('n = '))
i = 3
while i <= n:
    j = a[1]
    a[1] += a[0]
    a[0] = j
    i += 1
print(a[1])
