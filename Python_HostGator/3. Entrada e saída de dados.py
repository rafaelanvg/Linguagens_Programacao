## Entrada e Saída de dados

# Saída
nome = "Rafaela"
print(f"Olá, {nome}, tudo bem?")

# Entrada
nome = input()
print(f"Olá, {nome}, tudo bem?")

# Qual o preço barato?
preço_barato = input()

# Qual seria o preço ideal para você?
preço_barato = input("Qual seria o preço ideal para você?")
print(f"Tipo antigo: {type(preço_barato)}" )
preço_barato = float(preço_barato)
print(f"Tipo novo: {type(preço_barato)}" )

# Adicionando mais informações
gratuito = False
preço = 150.00

preço_barato = input("Qual seria o preço ideal para você?")
preço_barato = float(preço_barato)

preço_razoavel = float(input("E um preço razoável?"))

if gratuito:
    print("Legal, quero aprender agora!")
elif preço <= preço_barato:
    print("Quero comprar!")
elif preço < preço_razoavel:
    print("Deixa eu pensar uns 5 minutinhos")
else:
    print("Quem sabe no futuro, agora não posso!")