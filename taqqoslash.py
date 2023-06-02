# taqqoslash
x=float(input("birinchi sonni kiriting:"))
y=float(input("ikkinchi sonni kiriting:"))
z=float(input("uchinchi sonni kiriting:"))


if x>y and x>z:
    if y>z:
        print(f"{x}>{y}>{z}")
    else:
        print(f"{x}>{z}>{y}")

elif y>x and y>z:
     if x>z:
         print(f"{y}>{x}>{z}")
     else:
         print(f"{y}>{z}>{x}")
elif z>y and z>x:
    if y>x:
        print(f"{z}>{y}>{x}")
    else:
        print(f"{z}>{x}>{y}")
else:
    print(f"{z}={x}={y} sonlar teng")

        