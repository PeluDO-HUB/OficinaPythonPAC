"""
Crie um programa que solicite o nome e a idade de uma pessoa.
Depois, classifique-a como Criança, Adolescente ou Adulto,
de acordo com a idade, e exiba todas as informações
de forma organizada.
"""

nome = str(input("Digite o nome da pessoa: "))
idade = int(input("Digite a idade da pessoa: "))

if idade < 12:
    classificacao = "Criança"
elif idade < 18:
    classificacao = "Adolescente"
else:
    classificacao = "Adulto"

print(f" a pessoa se chama {nome}, tem {idade} anos e é classificada como {classificacao}.")
print(f"Resumo: \nNome: {nome} \nIdade: {idade} \nClassificação: {classificacao}")