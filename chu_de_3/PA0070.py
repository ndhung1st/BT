n = input("nhap: ")
for i in range(10):
    kt = 0
    for j in n:
        if j == str(i):
            kt += 1
    print("so chu so ", i, ": ", kt)
