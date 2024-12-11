
a= int(input())
b = int(input())
c = a
if b<1:
    print("gay")
else:
    while b>1:
        c = c*a
        b = b- b
    print(c)