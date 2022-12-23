n = input("nhap cau: ")
kt = False
for i in range(len(n)):
    if n[i: i + 8] == "Covid-19":
        kt = True
        break
if kt == True:
    print("YES")
else:
    print("NO")
