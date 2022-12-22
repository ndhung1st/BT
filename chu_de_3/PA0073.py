n = input("nhap: ")
h = 1
for i in n:
    if i != " ":
        print(i, end = '')
    else:
        print('')
        h += 1
print("\nso tu: ", h)
