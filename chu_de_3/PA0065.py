n = input("nhap tu: ")
np = ""
for i in range(-1, -len(n) - 1, -1):
    np += n[i]
if np == n:
    print("YES")
else:
    print("NO")
