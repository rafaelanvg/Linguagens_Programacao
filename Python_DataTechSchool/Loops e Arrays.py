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
