# Usando o if

vaiChover = "sim"
if(vaiChover == "sim"):
    print("pegar guarda-chuva")

vaiChover = "True"
if(vaiChover == "sim"):
    print("pegar guarda-chuva") 

vaiChover = "sim"
if(vaiChover):
    print("pegar guarda-chuva")

idade = 15
if(idade < 18):
    print("Você é menor de idade!")

nome = "Rafaela"
if(nome == "Rafaela"):
    print("Rafaela é Brasileira!")
    print("Rafaela mora em Fortaleza!") 

# Comparação entre valores
print(10 == 10)
print(9 >= 10)

# Usando o else
temAlguem = "sim"

if(temAlguem == "sim"):
    print("Luz")
else:
    print("Apagar")


idade = 15

if(idade >= 18):
    print("Você é menor de idade!")
else:
    print("Você é menor de idade!")

# Usando o elif
caminho = 3
if(caminho == 1):
    print("Escolhi o caminho 1!")
elif(caminho == 2):
    print("Escolhi o caminho 2!")
else:
    print("Escolhi o caminho 3!")

# Interagir com o computador através de condicionais
vaiChover = input("Vai chover? ")
print("O usuário disse:" + vaiChover)


vaiChover = input("Vai chover? ")
if(vaiChover == "sim"):
    print("Então pegue o guarda-chuva!")
else:
    print("Então não precisa do guarda-chuva!")

nome = input("Qual o seu nome?")
if(nome == "rafaela"):
    print("Olá Rafaela!")
elif(nome == "joao"):
    print("Olá, João!")
else:
    print("Olá " + nome + ", não te conheço!")

# Criando um mini chatbot
nome = input("Qual o seu nome?")
print("Olá " + nome)
idade = input("Qual a sua idade?")
idade = int (idade)
if(idade >= 18):
    dirigir = input("Qual transporte você gostaria de dirigir, quando tirar a carteira? carro, moto ou caminhão?")
    if(dirigir == "carro"):
        print("O preço para tirar a carteira de carro é R$100. Aproveite!")
    elif(dirigir == "moto"):
        print("O preço para tirar a carteira de moto é R$70. Aproveite!")
    elif(dirigir == "caminhão"):
        print("O preço para tirar a carteira de caminhão é R$150. Aproveite!")
    else:
        print("Não conheço esse transporte!")
else:
    print("Você tem menos de 18 anos e não pode tirar a carteira para dirigir ainda!")

