"""
05 – Escreva um programa em Python que pergunte a pontuação do jogador em cada uma das 10 fases do jogo. 
Dentro da repetição, o programa deve perguntar a pontuação de cada fase, e somar os pontos de cada fase em uma variável total. 
Depois da repetição, o programa deve mostrar esse total.
"""
pontuacao = 0
for fases in range(1,11):
    
    print(f"Qual sua pontuação na fase {fases}?")
    resposta = int(input())
    pontuacao = resposta + pontuacao
else:
    print(f"Sua pontuação total é de {pontuacao}")
