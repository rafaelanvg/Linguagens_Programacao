# Criar arquivos
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("\nNunca foi tao facil criar um arquivo.")

# Abrir para leitura
with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print("linha")