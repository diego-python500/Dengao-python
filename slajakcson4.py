
a = int(input("saralio nengue\n"))

if a <= 280:
    sf = a + a/5
    c = a/5
    b = 20
else:
    if a <= 700:
        sf = a + (a*15)/100
        c = (a*15)/100
        b = 15
    else:
        if a <= 1500:
            sf = a + a/10
            c = a/10
            b = 10
        else:
            sf = a + a/20
            c= a/20
            b= 5


print("salario antigo:", a ,"\n agora",sf, "\n aumento (%)", b, "\n aumento bruto", c )