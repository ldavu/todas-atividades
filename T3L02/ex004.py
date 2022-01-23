# 04 – Escreva um programa em Python que use números aleatórios para gerar jogos da mega sena. Gere 6 números entre 1 e 60.
import random

for controle in range(6):
    sorteio = random.randint(1,60)
    print(sorteio, end=", ")
