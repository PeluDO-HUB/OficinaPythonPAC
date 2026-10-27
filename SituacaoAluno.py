"""
Peça o nome do aluno e logo em seguida receba 3 ou mais notas, calcule a média e informe a situação do aluno
Reprovado: média menor que 5
Recuperação: média entre 5 e 7
Aprovado: média maior que 7
"""

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



