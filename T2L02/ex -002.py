jogador_saldo = 0

print("ola jogador! \n quai caixa você encontrou?")
resposta_Caixa = str(input(""))
print("você possui uma conta premium?")
resposta_ContaTipo = str(input(""))

#caixas: bronze prata ouro
'''
Caixa Bronze com conta Premium: ganha um item incomum e 500 moedas.
- Caixa Bronze sem conta Premium: ganha um item comum e 250 moedas.
- Caixa Prata com conta Premium: ganha um item raro e 1000 moedas.
- Caixa Prata sem conta Premium: ganha o mesmo que bronze premium.
- Caixa Ouro com conta Premium: ganha um item lendário e 5000 moedas.
- Caixa Ouro sem conta Premium: ganha o mesmo que prata premium.
'''

if (resposta_Caixa == "Bronze") and (resposta_ContaTipo == "sim"):
    print("Você ganhou um item incomum e 500 moedas!")

if (resposta_Caixa == "Bronze") and (resposta_ContaTipo in ['n','não',"não"]):
    print("parabén você ganhou um item comum e 250 moedas")

if (resposta_Caixa == "Prata") and (resposta_ContaTipo in ['s','sim']):
    print("você ganhou uma caixa rara e 1000 moedas!")

if (resposta_Caixa == "Prata") and (resposta_ContaTipo in ['n','não']):
    print("Você ganhou um item incomum e 500 moedas!")

if (resposta_Caixa == "Ouro") and (resposta_ContaTipo in ['s','sim']):
    print('você ganhou um item lendário e 5000 moedas!')

if (resposta_Caixa == "Ouro") and (resposta_ContaTipo in ['n','não']):
    print('você ganhou uma caixa rara e 1000 moedas!')
