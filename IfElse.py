"""
1.
Peça o nome do aluno e logo em seguida receba 3 ou mais notas, calcule a média e informe a situação do aluno
Reprovado: média menor que 5
Recuperação: média entre 5 e 7
Aprovado: média maior que 7
"""




senha = "012345"
senhaTentativa = str(input("Digite a senha: "))

if senha == senhaTentativa:
    print("Login feito com sucesso!")
else:
    print("falhou no login :(")
 


def situacaoAluno():
    nome =str(input("Insira o nome do Aluno: "))
    nota1 =float(input("Insira a primeira nota:"))
    nota2 =float(input("Insira a Segunda nota:"))
    nota3 =float(input("Insira a Terceira nota:"))

    media = (nota1 + nota2 + nota3) / 3

    if media < 5:
        print(f"O aluno {nome} foi reprovado com a nota {media:.2f}")
    elif media>=5 and media<7: 
        print(f"O aluno {nome} está de recuperação com a nota {media:.2f}")
    elif media>=7:
        print(f"O aluno {nome} foi aprovado com a nota {media:.2f}")

"""
2.
Crie um programa que solicite o nome e a idade de uma pessoa.
Depois, classifique-a como Criança, Adolescente ou Adulto,
de acordo com a idade, e exiba todas as informações
de forma organizada.
"""

def classifacaoIdade():

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

"""
3.
Crie um programa que solicite a idade de uma pessoa e classifique
o valor do ingresso conforme as regras:
    Menor que 12 anos o ingresso será de R$12.00
    12 a 17 anos o ingresso será de R$15.00
    Acima de 18 anos o ingresso será de R$25.00
"""

def classificacaoIngresso():
    idade = int(input("Digite sua idade para verificar o valor do ingresso: "))
    
    if idade >= 0 and idade < 12 :
        print("Ingresso Infantil - R$12.00")
    elif idade >=12 and idade < 18:
        print("Ingresso Juvenil - R$15.00")
    elif idade >= 18:
        print("Ingresso Adulto - R$25.00")
    else :
        print("Idade Invalida!")

