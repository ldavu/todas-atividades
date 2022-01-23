print("Olá thanos, quais joias do infinito você possui?")

#jóia do espaço, jóia da mente, jóia da realidade, jóia do poder, jóia do tempo, jóia da alma.
joia1 = "Espaço" , False
joia2 = "Mente", False
joia3 = "Realidade", False
joia4 = "Poder", False
joia5 = "Tempo", False
joia6 = "alma", False

print("Responda as perguntas com sim ou não.")

print("Você possui a joia do espaço?")
resposta = str(input(""))
if resposta in ['s','sim']:
    joia1 = True

print("Você possui a joia da mente?")
resposta = str(input(""))
if resposta in ['s','sim']:
    joia2 = True

print("Você possui a joia da realidade?")
resposta = str(input(""))
if resposta in ['s','sim']:
    joia3 = True

print("Você possui a joia do poder?")
resposta = str(input(""))
if resposta in ['s','sim']:
    joia4 = True

print("Você possui a joia do tempo?")
resposta = str(input(""))
if resposta in ['s','sim']:
    joia5 = True

print("Você possui a joia da alma?")
resposta = str(input(""))
if resposta in ['s','sim']:
    joia6 = True

if (joia1 == True) and (joia2 == True) and (joia3 == True) and (joia4 == True) and (joia5 == True) and (joia6 == True):
    print("você possui todas as joias, ja pode dizimar o mundo!")
else:
    print("você não possui todas as joias!")
