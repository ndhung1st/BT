def snt(n):
	if n == 0 or n == 1:
		return False
	elif n == 2:
		return True
	else:
		for i in range(2, int(n ** (1 / 2) + 1)):
			if n % i == 0:
				return False
	return True
a = 2
b = 3
while b < 1000:
	if b - a == 2:
		print(f'({a}, {b})', end = ' ')
	a = b
	while True:
		b += 1
		if snt(b) == True:
			break