a = (input("digite o primeiro numero\n"))
b = (input("digite o segundo numero\n"))
c = (input("digite o terceiro numero\n"))

if a > b and c:
    print(a)
    if c > b: 
        print("1:", a ,"\n2:", c ,"\n3:", b)
    else:
        print("\n1:", a, "\n2:",b, "\n3:", c)

if b > a and c:
    print(b)
    if c > a: 
        print("\n1:", b ,"\n2:", c ,"\n3:", a)
    else:
        print("\n1:",b ,"\n2:",a ,"\n3:", c)
else:
    print(c)
    if a > b: 
        print("\n1:", c ,"\n2:", a ,"\n3:", b)
    else:
        print("\n1:",c ,"\n2:",b ,"\n3:", a)


