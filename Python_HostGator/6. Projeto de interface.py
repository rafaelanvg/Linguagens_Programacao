#### Implementando a interface dos pedidos

nome = input("Como gostaria de ser chamado(a)")
categorias = ["Wordpress",
              "Criação de Site",
              "E-commerce",
              "Marketing Digital",
              "Vendas",
              "Google Ads",
              "Design",
              "Negócios",
              "Youtube",
              "Criação de Conteúdo",
              "Programação"]

for i in range(len(categorias)):
  # equivalente a usar enumerate
  print(f"{i}. {categorias[i]}")

num_das_categorias = input(
    "Digite o número dos assuntos de seu interesse (use vírgulas):\n"
    )

# TODO: resolver problema num_das_categorias = "10, 8"

tempo = float(input("Quanto tempo gostaria de estudar? (min)\n"))

mostrar_premium = input("Mostrar cursos Premium (S/N)?")

gratuidade = [True,
              True,
              True,
              True,
              True,
              True,
              True,
              True,
              True,
              False,
              True,]

#### Resolvendo problemas com tipos de dados
print(type(nome))
print(type(num_das_categorias))
print(type(tempo))
print(type(mostrar_premium))

if mostrar_premium == "N" or gratuidade == "n":
  mostrar_premium = False
else:
  mostrar_premium = True

num_das_categorias = num_das_categorias.split(",")
ncategorias = []
for elemento in num_das_categorias:
  numero = int(elemento.strip())
  ncategorias.append(numero)

print(ncategorias)

print(f"Nome: {nome}")
print(f"ID das Categorias: {ncategorias}")
print(f"Tempo: {tempo}")
print(f"Mostrar Premium?: {mostrar_premium}")

#### Analisando o perfil de interesses
# Colunas da tabela na forma de listas
cursos = ["Introdução ao Wordpress",
          "Criador de Sites",
          "Introdução ao WooCommerce",
          "Afiliado de Sucesso",
          "Venda mais com WhatsApp Business e Google Meu Negócio",
          "Introdução ao Google Ads",
          "E-commerce e Vendas Online",
          "Canva: Design Fácil para Empreendedores",
          "Youtube para Iniciantes: como criar e crescer o seu canal",
          "Rede de Display e Youtube",
          "Desenvolvimento de Plugins para WordPress"
          ]

tempos = [95,
          25,
          35,
          85,
          75,
          150,
          140,
          120,
          85,
          335,
          160]

categorias_do_curso = [
  ['wordpress', 'criação de sites'],
  ['criação de sites'],
  ['e-commerce', 'criação de sites', 'wordpress'],
  ['marketing digital', 'vendas'],
  ['marketing digital', 'vendas', 'google ads', 'negócios'],
  ['marketing digital', 'google ads'],
  ['e-commerce', 'vendas', 'negócios'],
  ['design', 'negócios'],
  ['youtube', 'criação de conteúdo'],
  ['marketing digital', 'google ads', 'youtube'],
  ['programação', 'wordpress']
]

# Categorias selecionadas
categorias_selecionadas = []
for n in ncategorias:
  categorias_selecionadas.append(categorias[n].upper())

print(categorias_selecionadas)

print(f"Olá, {nome}, com base no seu perfil, achamos que você iria gostar dos seguintes cursos:")
for cat in categorias_selecionadas:
  print(f"{cat}:")
  for linha in range(len(cursos)):
    if gratuidade[linha] or mostrar_premium:
      if (cat.lower() in categorias_do_curso[linha]
          and tempos[linha] <= tempo):
        print(f"– {cursos[linha]} ({tempos[linha]} min)")