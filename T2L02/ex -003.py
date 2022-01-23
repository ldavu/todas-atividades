'''
O evento DRIFT é para carros de tração traseira com pneus nível mínimo de 5.-----------------
- O evento SPRINT é para carros de tração dianteira com transmissão mínimo nível 3.---------------
- O evento CIRCUITO é para carros de tração traseira ou dianteira, com motor mínimo nível 4. ------
- Pergunte ao jogador ou jogadora qual a tração do seu carro, qual o nível de pneus, nível de transmissão e nível de motor.
- Depois informe qual o evento que ele poderá participar, inclusive informando caso ele não possa participar de nenhum evento ainda.
'''

print('Qual a tração do seus carro? Traseira | Dianteira')
resposta_Tracao = input()

print("Qual o nivel de seus pneus?")
resposta_pneus = int(input())

print("Qual o nivel de transmissão?")
resposta_Transmissão = input()

print("Qual o nivl do seu motor?")
resposta_motor = input()

if (resposta_Tracao in ['traseira','dianteira']) and (resposta_pneus >= 5) and (resposta_Transmissão <= 0) and (resposta_motor == 4):
    print("Você pode participar do evento Circuito!")

elif (resposta_Tracao == "traseira") and (resposta_pneus >= 5):
    print("Você pode partiipar do evento Drift!")
elif (resposta_Tracao == "dianteira") and (resposta_Transmissão >= 3):
    print('Você pode participar do evento Sprint!')

else:
    print("Não possui nenhum evento ainda para seu tipo de carro!")