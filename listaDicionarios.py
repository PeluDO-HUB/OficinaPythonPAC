### git config --local credential.helper "" lembrar de passar ao final da aula
# ==================================================
# 1. LISTAS (LIST)
# ==================================================

# Criando uma lista com alguns produtos
produtos = ["Mouse", "Teclado", "Monitor"]




"""Acessando elementos pelo índice
Lembre-se: o primeiro elemento está no índice 0"""
print(produtos[0])  
print(produtos[1])  

""" ADICIONANDO ELEMENTOS

# append() adiciona um elemento ao final da lista"""
produtos.append("Headset")

# insert() adiciona um elemento em uma posição 
# específica
produtos.insert(1, "Webcam")

# REMOVENDO ELEMENTOS

# remove() remove um elemento pelo seu valor
produtos.remove("Mouse")

# pop() remove um elemento pelo seu índice
removido = produtos.pop(1)
print("Produto removido:", removido)

# ALTERANDO ELEMENTOS

# Altera o valor de um elemento utilizando seu índice
produtos[0] = "Teclado Gamer"

# CONSULTANDO A LISTA

# len() retorna a quantidade de elementos
print("Quantidade de produtos:", len(produtos)) # 4

# in verifica se determinado elemento existe
if "Monitor" in produtos:
    print("Monitor encontrado!")

# for percorre todos os elementos da lista
print("\n=== LISTA DE PRODUTOS ===")

for produto in produtos:
    print(produto)

"""
1. Listas — Lista de compras
Crie um programa que permita organizar uma lista de compras.
O programa deve: 
    Criar uma lista vazia chamada compras.
    Adicionar 3 produtos utilizando append().
    Adicionar mais um produto na segunda posição utilizando insert().
    Exibir todos os produtos utilizando for.
    Remover um produto utilizando remove().
    Exibir todos os produtos utilizando for.
    Mostrar quantos produtos existem na lista utilizando len().
"""

def listaCompras():
    lista = []
    lista.append("Tomate")
    lista.append("Limão")
    lista.append("Banana")
    lista.insert(1,"Uva")
    print("Foi adicionado nessa ordem, tomate, limão, banana e uva sendo o insert na segunda " \
        "posição")
    for items in lista:
        print(items)
    lista.remove("Tomate")
    for items in lista:
        print(items)
    print(len(lista))


# ==================================================
# 2. DICIONÁRIOS (DICT)
# ==================================================

# Criando um dicionário com informações de um aluno
aluno = {
    "nome": "Pedro",
    "idade": 25,
    "nota": 8.5
}

# ACESSANDO INFORMAÇÕES

# Acessamos os valores utilizando suas respectivas chaves
print("\nNome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Nota:", aluno["nota"])

# ADICIONANDO INFORMAÇÕES

# Se a chave não existir, uma nova informação será criada
aluno["curso"] = "Python"

# ALTERANDO INFORMAÇÕES

# Se a chave já existir, seu valor será substituído
aluno["nota"] = 9.0

# REMOVENDO INFORMAÇÕES

# pop() remove uma chave e seu respectivo valor
aluno.pop("idade")

# Também podemos utilizar del para excluir uma chave
del aluno["curso"]

# CONSULTANDO INFORMAÇÕES

# get() consulta uma chave sem gerar erro caso ela não exista
print("\nNome:", aluno.get("nome"))

# Se a chave não existir, podemos definir uma mensagem padrão
print("Idade:", aluno.get("idade", "Não cadastrada"))

# in verifica se determinada chave existe
if "nota" in aluno:
    print("Nota cadastrada!")

# PERCORRENDO O DICIONÁRIO

# items() permite acessar a chave e o valor simultaneamente
print("\n=== INFORMAÇÕES DO ALUNO ===")

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

"""
2. Dicionários — Cadastro de um produto
Crie um dicionário para armazenar as informações de um produto.
O programa deve:
    Armazenar nome, preço, quantidade e categoria.
    Exibir todas as informações do produto.
    Alterar o preço do produto.
    Adicionar uma nova informação chamada marca.
    Remover a informação categoria.
    Exibir novamente todas as informações utilizando items().
"""
def cadastroProdutoDic():
    produto={
        "nome":"Fanta Uva 2L",
        "preco":10.50,
        "qtd":5,
        "categoria":"Bebida"}
    
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")
    
    produto["preco"] = 8.90
    produto["marca"] = "Coca-Cola"
    del produto["categoria"]
    print()
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")
        




# ==================================================
# 3. LISTA DE DICIONÁRIOS
# ==================================================

# Criando uma lista que armazena vários dicionários
# Cada dicionário representa um aluno

alunos = [
    {
        "nome": "Ana",
        "idade": 17,
        "nota": 8.5
    },
    {
        "nome": "João",
        "idade": 18,
        "nota": 7.0
    },
    {
        "nome": "Maria",
        "idade": 16,
        "nota": 9.5
    }
]

# ACESSANDO INFORMAÇÕES

# Primeiro acessamos o índice da lista
# Depois acessamos a chave do dicionário

print("\nPrimeiro aluno:", alunos[0]["nome"])
print("Nota do segundo aluno:", alunos[1]["nota"])

# ADICIONANDO UM NOVO ALUNO

novo_aluno = {
    "nome": "Carlos",
    "idade": 19,
    "nota": 6.5
}

# append() adiciona o novo dicionário à lista
alunos.append(novo_aluno)

# TAMBÉM PODEMOS ADICIONAR DIRETAMENTE

alunos.append({
    "nome": "Pedro",
    "idade": 20,
    "nota": 8.0
})

# LISTANDO TODOS OS ALUNOS

print("\n=== LISTA DE ALUNOS ===")

# O for percorre a lista
# A cada repetição, aluno recebe um dicionário

for aluno in alunos:
    print("----------------------")
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Nota:", aluno["nota"])

# ALTERANDO INFORMAÇÕES DE UM ALUNO

# Acessamos o índice da lista e depois a chave
alunos[0]["nome"] = "Ana Clara"
alunos[0]["nota"] = 10.0

# Também podemos adicionar uma nova informação
alunos[0]["curso"] = "Python"

# REMOVENDO UM ALUNO

# pop() remove o dicionário inteiro pelo índice
alunos.pop(1)

# REMOVENDO UMA INFORMAÇÃO DE UM ALUNO

# pop() também pode remover uma chave do dicionário
alunos[0].pop("curso")

# BUSCANDO UM ALUNO PELO NOME

nome_busca = input("\nDigite o nome do aluno para buscar: ")

for aluno in alunos:

    # lower() permite comparar sem diferenciar maiúsculas
    # e minúsculas, transformando todo o texto em minúsculo
    if aluno["nome"].lower() == nome_busca.lower():

        print("\nAluno encontrado!")
        print("Nome:", aluno["nome"])
        print("Idade:", aluno["idade"])
        print("Nota:", aluno["nota"])

        break

else:
    # O else do for é executado quando o laço termina
    # sem encontrar nenhum break
    print("Aluno não encontrado!")

# MOSTRANDO A QUANTIDADE DE ALUNOS CADASTRADOS
#len() mostra a quantidade de itens possui dentro da lista
print("\nTotal de alunos:", len(alunos))


"""   
3. Lista de dicionários — Controle de estoque
Crie um programa para organizar os produtos de uma loja.
Cada produto deverá possuir:
    - Nome
    - Preço
    - Quantidade em estoque
O programa deverá:
    Criar uma lista chamada estoque contendo pelo menos 3 produtos.
    Exibir o nome e a quantidade de cada produto utilizando for.
    Adicionar um novo produto à lista.
    Alterar a quantidade em estoque de um produto existente.
    Remover um produto da lista.
    Exibir todos os produtos e seus respectivos preços.
Desafio extra (opcional): percorrer a lista e informar quais produtos possuem 
menos de 5 unidades em estoque.
"""
def controleEstoque():
    estoque=[
        {
            "nome":"Fanta Uva 2L",
            "preco":10.50,
            "qtd":5
        },
        {
            "nome":"Coca-Cola 2L",
            "preco":14.50,
            "qtd":2
        },
        {
            "nome":"Guarana Antartica 2L",
            "preco":8.50,
            "qtd":10
        }
        ]
    for produto in estoque:
        print("----------------------")
        print("Nome:", produto["nome"])
        print("Nota:", produto["qtd"])

    estoque.append({"nome":"Bolacha Trakinas","preco":3.50,"qtd":25})

    estoque[0]["qtd"]= 2

    del estoque[2]
    for produto in estoque:
        print("----------------------")
        print("Nome:", produto["nome"])
        print("Preço:", produto["preco"])

    """
    desafio
    """
    for produto in estoque:
        if produto["qtd"] < 5:
            print(f"O produto {produto['nome']} possui menos de 5 unidades no momento!! "
                    f"Qtd Atual: {produto['qtd']}")
                    
