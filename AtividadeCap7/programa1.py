time = float(input("Tempo como fumante (em anos).....: "))
value = float(input("Valor do maço...................: "))
amountPerDay = float(input("Quantidade de maços por dia.....: "))
daysPerYear = float(360)

amountSpent = (daysPerYear * time) * (value * amountPerDay)

if amountSpent < 20000.00:
    print(f"Com o valor R$ {amountSpent:.2f}, você poderia ter dado entrada em um carro.")
elif amountSpent <= 50000.00:
    print(f"Com o valor R$ {amountSpent:.2f}, você poderia ter comprado um carro popular usado.")
elif amountSpent > 50000.00:
    print(f"Com o valor R$ {amountSpent:.2f}, você poderia ter comprado um carro zero.")