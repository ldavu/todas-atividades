import random

print("Tempo final dos carros: \n==========================")

for carro in range(1,21):
    
    if carro == 1:
        tempo1 = random.randint(100,110)
        print(f"Tempo do carro {carro}: {tempo1}")
    else:
        tempo2 = random.randint(1,10)

        tempo1 += tempo2
        print(f"Tempo do carro {carro}: {tempo1}s (+{tempo2})")
