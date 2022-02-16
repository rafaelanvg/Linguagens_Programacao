# Funções 
def funcao_que_fala_oi():
    print("oi")

funcao_que_fala_oi()

# Função com parâmetros

def funcao_que_fala_oi_para_pessoa(nome):
    print("Olá " + nome)
funcao_que_fala_oi_para_pessoa("José") 


def fazer_carne_moida(tipo_da_carne):
    print("Carne moida feita a partir da carne de:" + tipo_da_carne)
fazer_carne_moida("vaca")


def entrada_no_restaurante(nome, idade):
    if(idade >= 18):
        print("Seja bem vindo! " + nome)
    else:
        print(nome + ", você não pode entrar no restaurante, pois é menor de idade!")

entrada_no_restaurante ("Rafa", 17)


def somar(numero1, numero2):
    resultado = numero1 + numero2
    print("Resultado é igual a: " + str(resultado))

somar(50,30)

# Retornando valores 

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print(somar(10,20))


def area_do_circulo(raio):
    pi = 3.14
    area = pi*raio**2
    return area
print(area_do_circulo(10))
