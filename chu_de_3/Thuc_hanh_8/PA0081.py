n = int(input('n = '))
arr = []
while n > 1:
    if n % 2 == 1:
        arr.append(str(1))
        n //= 2
    else:
        arr.append(str(0))
        n //= 2
print("1", end = '')
for i in range(-1, -len(arr) - 1, -1):
    print(arr[i], end = '')