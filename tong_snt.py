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
n = int(input('n = '))
for i in range(2, int(n / 2) + 1):
	if snt(i) == True and snt(n - i) == True:
		print(i,' ', n - i)