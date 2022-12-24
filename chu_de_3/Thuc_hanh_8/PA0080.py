def snt(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    else:
        i = 2
        while i <= int(n ** (1 / 2)) + 1:
            if n % i == 0:
                return False
            i += 1
    return True
def ucln(a, b):
    while True:
        if a == b:
            return a
        elif a > b:
            a -= b
        else:
            b -= a
n = int(input('n = '))
i = 1
a = []
while i <= n:
    a.append(int(input(f"a[{i}] = ")))
    i += 1
dem = 0
for i in a:
    if snt(i) == True:
        dem += 1
print("- So luong so nguyen to: ", dem)
uc = a[0]
for i in a:
    uc = ucln(uc, i)
print('- UCLN: ', uc)