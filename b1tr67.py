def ucln(a,b):
	while True:
		if a == b:
			return a
		elif a > b:
			a -= b
		else:
			b -= a
n = int(input('n = '))
a = int(input(f'nhap so thu {1}: '))
uc = a
for i in range(2, n + 1):
	j = int(input(f'nhap so thu {i}: '))
	uc = ucln(uc, j)
print(uc)