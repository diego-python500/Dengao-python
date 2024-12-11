import json
3
print("primeiro escolha sua operação")

print("+ = 1")
print("- = 2")
print("* = 3")
print(": = 4")
cauculo = input()
print("qual é o primeiro numero")
num1 = input()
print("qual é o segundo numero")
num2 = input()
if cauculo== 1:
    resultado = num1 + num2
    print("o resultado é", resultado)
if cauculo== 2:
    resultado = num1 - num2
    print("o resultado é", resultado)
if cauculo== 3:
    resultado = num1 * num2
    print("o resultado é", resultado)
if cauculo== 3:
    resultado = num1/num2
    print("o resultado é", resultado)
