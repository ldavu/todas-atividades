"""
06 – Escreva um programa em Python que use números aleatórios para gerar o tempo de entrega de um entregador de pizzas. Dentro da repetição, 
o programa deve gerar os tempos de entrega de 10 pizzas diferentes, que deve ser entre 20 e 60, e depois mostrar cada um desses tempos. 
Além disso, deve somar cada tempo em uma variável total. Depois da repetição, o programa deve mostrar o tempo total do trabalho do entregador.
"""
import random

tempoTotal = 0
for entregas in range(1,11):
    tempoDeEntrega = random.randint(20,60)
    print(f"--------------\nEntrega de número: {entregas}\nTempo da entrega: {tempoDeEntrega} Minutos \n--------------\n")
    tempoTotal = tempoTotal + tempoDeEntrega


print(f"Tempo total de: {tempoTotal}")
