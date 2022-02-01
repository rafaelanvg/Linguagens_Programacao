# lista de Strings

lista_de_nomes = ["Maria","José","João"]
lista_precos = [10.45,100.25,2.5]

print(lista_de_nomes[2])
print(lista_precos[2])

# lista de inteiros

lista = [1, 1, 2, 3, 5]

# lista vazia

lista = []

lista_de_nomes = []
lista_de_nomes = list()

lista_de_nomes.append("Maria")
lista_de_nomes.append("José")
print(lista_de_nomes)

lista_de_nomes.remove("José")
print(lista_de_nomes)

# Laços For

lista_de_elementos = ["Mara", "Joana", "Bete"]
print(lista_de_elementos[1])

for elemento in lista_de_elementos:
    print(elemento)

# Usando números

lista_de_numeros = [1,2,3,4,5]
print(lista_de_numeros[1])

# Pode usar o range para não ter que escrever tudo

lista_de_numeros = [1,2,3,4,5] 
lista_de_numeros = range(1,5)
print(lista_de_numeros[2])

# Usando o for 

lista_de_numeros = range(1,200)
for elemento in lista_de_numeros:
    print(elemento)

# Repetições sobre condição

continuar = "sim"

while(continuar == "sim"):
    print("oi")
    continuar = input("Deseja continuar?")
print("Saio do loop")

# Mini chatbot para criar uma lista de convidados

continuar = "sim"
lista_de_convidados = []

while(continuar == "sim"):
    nome = input("Quem vem para a festa?")
    if(nome == "Joao"):
        print("Eu não posso convidar o João!")
    else:
        lista_de_convidados.append(nome)

    continuar = input("Alguém mais vem para a festa? Opções: sim ou não") 

print("Lista de convidados:")
print(lista_de_convidados)

# Fazendo um sistema de caixa eletrônico

"""
Transações bancárias, criando um caixa eletrônico com operações sobre uma variável de saldo. 

O Sistema deve:
- Mostrar saldo da conta (iniciado com R$1000)
- Fazer um saque e atualizar valor do saldo (não pode permitir saques maiores que o saldo)
- Fazer depósito (inserir dinheiro)
- Sair
*Faça operação continuar até a pessoa escolher uma opção de saida.
"""
saldo = 1000
continuar = "sim"

while(continuar == "sim"):
    operacao = input("Qual operação você quer realizar? Opções: saldo, sacar, depositar e sair")
    if(operacao == "saldo"):
        print("Seu saldo é " + str(saldo))
    elif(operacao == "sacar"):
        valor_do_saque = input("Qual valor você quer sacar?")
        valor_do_saque = int(valor_do_saque)
        saldo = saldo - valor_do_saque
    elif(operacao == "depositar"):
        valor_do_deposito = input("Qual valor você quer depositar?")
        valor_do_deposito = int(valor_do_deposito)
        saldo = saldo + valor_do_deposito
    elif(operacao == "sair"):
        print("Obrigado! Até Breve!")
        continuar = "nao"
    else:
        print("Operação não reconhecida")
    
    




