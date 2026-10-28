"""Exercícios — Laços de repetição em Python
1. Contagem regressiva — while
Faça um programa que mostre uma contagem regressiva de 10 até 1. Ao final, exiba a mensagem "Fim!".
"""


def contagemRegressiva():
    contador = 10
    print("Iniciando contagem Regressiva...")
    while contador>0:
        print(contador)
        contador= contador-1

"""
2. Senha correta — while
Faça um programa que peça ao usuário para digitar uma senha.
Enquanto a senha estiver incorreta, peça para digitar novamente. Quando acertar, exiba "Acesso permitido!".
Considere a senha correta como 01234.
"""

def senhaCorreta():
    senha ="01234"
    senha2 = str(input("Digite sua senha: "))

    while senha != senha2 :
        senha2= str(input("Senha Incorreta, Digite novamente: "))

    """
    Para mostrar como utilizar o while para evitar um erro.
    while True:
        senha2= str(input("Digite a senha: "))
        if senha == senha2:
            break
        else:
            print("Senha Incorreta!")
    """
    print("Login Feito com Sucesso!")


"""
3. Tabuada — for e range()
Peça ao usuário um número inteiro e mostre a tabuada desse número, de 1 a 10.
"""
def tabuadaFor():
        
    num = int(input("Digite um número inteiro para ver sua tabuada: "))
    print(f"Tabuada do {num}:")
    for i in range(1,11,1):
        print(f"{num} x {i} = {num*i}")

    print("Finalizada")



"""
4. Números pares — for e range()
Faça um programa que mostre todos os números pares de 0 até 20, utilizando for e range().
"""
def pares():
    for i in range(2,21,2):
        print(i)

"""
5. Soma dos números — for e range()
Peça ao usuário um número inteiro positivo.
Calcule e mostre a soma de todos os números de 1 até o número informado.
Exemplo: se o usuário digitar 5, o resultado será 15 (1 + 2 + 3 + 4 + 5).
"""

def somaNumeros():
    print("Digite um número, ele será somado com todos os anteriores até chega nele: ")
    print("Exemplo: se o usuário digitar 5, o resultado será 15 (1 + 2 + 3 + 4 + 5).")
    num= int(input(""))

    soma = 0
    for i in range(0,num+1,1):
        soma+=i

    print(f"Soma de todos os números deu: {soma}")
"""
6. Desafio — while e validação
Faça um programa que peça números inteiros ao usuário. 
O programa deve continuar recebendo números até que o usuário digite 0. 
Ao final, mostre a soma de todos os números digitados, sem contar o zero.
"""
def somador():
    print("Somador")
    num=int(input("Insira o primeiro número para iniciar as somas: "))
    soma = num

    while num!=0 :
        num= int(input("Adiciona mais um número a ser somado: "))
        soma+=num

    print(f"A soma de todos os números foi de: {soma}")



"""
print("Olá")
print("Olá")    
print("Olá")
print("Olá")
print("Olá")


contador = 0
while contador<=3:
    contador += 1
    print(f"Olá {contador}")


for i in range(3):
    print(f"Print {i+1}")

for i in range(12,17):
    print(f"Print {i}")


for i in range(14,517,20):
    print(f"Print {i}")
"""