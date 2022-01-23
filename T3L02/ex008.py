"""
08 – Escreva um programa em Python que monte uma variável com a lista de chamada de uma turma de 10 estudantes. 
Dentro da repetição, o programa deve perguntar o nome de cada estudante, e perguntar se o/a estudante está presente ou não. 
Depois, deve concatenar (acrescentar) as informações respondidas à variável da chamada. Depois da repetição, 
o programa deve mostrar a lista de chamada completa. Exemplo:
1 – Maria: presente
2 – José: presente
3 – Ana: ausente
4 – Marcos: presente

"""
chamada = ""

for estudante in range(1,11):
    nome = input(f'Qual o nome do {estudante}° aluno? \n')
    presença = input("Está presente ou ausente? \n")
    chamada = chamada + nome + " : " + presença + "\n"

print(chamada)
