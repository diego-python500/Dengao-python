import random
import os
import sys

def jogar_adivinhar_numero():
    print("Bem-vindo ao jogo de adivinhar o número!")
    print("Eu estou pensando em um número entre 1 e 10.")
    
    # O computador escolhe um número aleatório entre 1 e 10
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    acerto = False

    while not acerto:
        # O jogador faz um palpite
        palpite = input("Qual é o seu palpite? ")
        
        # Verifica se a entrada é um número válido
        if not palpite.isdigit():
            print("Por favor, insira um número válido.")
            continue
        
        palpite = int(palpite)
        tentativas += 1

        # Compara o palpite com o número secreto
        if palpite < numero_secreto:
            print("O número secreto é maior.")
        elif palpite > numero_secreto:
            print("O número secreto é menor.")
        else:
            acerto = True
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            print("O computador vai desligar agora...")
            os.system("shutdown -h now")

# Chama a função para iniciar o jogo
jogar_adivinhar_numero()
