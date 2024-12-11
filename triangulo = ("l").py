a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))




def classificar_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "Lados inválidos"
    return ("Equilátero" if a == b == c else
            "Isósceles" if a == b or a == c or b == c else
            "Escaleno")




print(classificar_triangulo(a, b, c))