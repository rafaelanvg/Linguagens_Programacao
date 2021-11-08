## Analisando condições. Decisão - if e else

# Se for verdadeiro vai aparecer na tela!
gratuito = True

if gratuito:
    print("Obá! Quero aprender agora!")
else:
    print("Hum...será que posso pagar?")

# Se for falso vai aparecer na tela!
gratuito = False

if gratuito:
    print("Obá! Quero aprender agora!")
else:
    print("Hum...será que posso pagar?")

# Adicionando elif

gratuito = False
preço = 70.00

if gratuito:
    print("Legal, quero aprender agora!")
elif preço < 100.00:
    print("Quero comprar!")
else:
    print("Quem sabe no futuro, agora não posso!")

# Aumentando o preço

gratuito = False
preço = 100.00

if gratuito:
    print("Legal, quero aprender agora!")
elif preço < 100.00:
    print("Quero comprar!")
else:
    print("Quem sabe no futuro, agora não posso!")

# Usando condição <=

gratuito = False
preço = 100.00

if gratuito:
    print("Legal, quero aprender agora!")
elif preço <=100.00:
    print("Quero comprar!")
else:
    print("Quem sabe no futuro, agora não posso!")

# Adicionando outra informação

gratuito = False
preço = 200.00

if gratuito:
    print("Legal, quero aprender agora!")
elif preço <= 100.00:
    print("Quero comprar!")
elif preço < 250.00:
    print("Deixa eu pensar uns 5 minutinhos")
else:
    print("Quem sabe no futuro, agora não posso!")