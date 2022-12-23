n = int(input("n = "))
a =[]
for i in range(n):
    a.append(float(input(f"ban thu {i + 1}: ")))
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            k = a[i]
            a[i] = a[j]
            a[j] = k
for i in a:
    print(i, end = ' ') 
    