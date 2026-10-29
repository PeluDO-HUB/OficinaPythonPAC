"""# Projeto Final de Python — Sistema de Cadastro de Alunos

## Objetivo
Desenvolver um programa em Python para cadastrar alunos,
armazenar suas informações, calcular suas médias e consultar suas situações escolares.

## Requisitos do projeto

O programa deverá apresentar um menu com as seguintes opções:

1. **Cadastrar aluno:** solicitar nome, idade, primeira nota e segunda nota.
2. **Listar alunos:** exibir todos os alunos cadastrados, com seus nomes, idades e notas.
3. **Consultar médias e situações:** calcular a média de cada aluno e informar sua situação escolar.
4. **Sair:** encerrar o programa.

## Regras de funcionamento

- A média deverá ser calculada utilizando as duas notas informadas.
- A situação escolar deverá seguir os seguintes critérios:
  - Média menor que 5: **Reprovado**.
  - Média igual ou maior que 5 e menor que 7: **Recuperação**.
  - Média igual ou maior que 7: **Aprovado**.
- O menu deverá continuar aparecendo até que o usuário escolha a opção de sair.
- Os dados de cada aluno deverão ser armazenados durante a execução do programa.
- O sistema deverá informar caso o usuário escolha uma opção inexistente no menu.

## Conteúdos que deverão ser utilizados

- Variáveis e tipos de dados.
- Entrada e saída de dados com `input()` e `print()`.
- Conversão de tipos com `int()` e `float()`.
- Estruturas condicionais: `if`, `elif` e `else`.
- Estruturas de repetição: `while`, `for` e `range()`.
- Listas e dicionários.
- Funções para organizar as funcionalidades do programa.

## Entrega

O projeto deverá funcionar no terminal e apresentar um menu organizado e fácil de utilizar. 
Ao final, os alunos deverão demonstrar o funcionamento do sistema e explicar como utilizaram os conteúdos 
estudados durante as aulas.

**Desafio extra (opcional):** impedir o cadastro de notas menores que 0 ou maiores que 10 
e permitir pesquisar um aluno pelo nome."""



alunos = []

print(len(alunos))
def cadastrar_aluno():
    print("\n--- CADASTRAR ALUNO ---")

    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    nota1 = float(input("Primeira nota: "))
    while nota1 <0 or nota1>10:
        print(f"Primeira nota inserida Invalida! Notas Aceitas de 0 a 10")
        nota1 = float(input("Primeira nota: "))

    nota2 = float(input("Segunda nota: "))
    while nota2 <0 or nota2>10:
        print(f"Segunda nota inserida Invalida! Notas Aceitas de 0 a 10")
        nota2 = float(input("Segunda nota: "))
    
        

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota1": nota1,
        "nota2": nota2
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")
    denovo=input("Deseja Cadastrar outro aluno? Sim ou S para cadastrar,caso não so aperte Enter").lower()
    if denovo=="sim" or denovo =="s":
        cadastrar_aluno()



def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print(f"{"Nome do Aluno".ljust(15)} | {"Nota 1".ljust(8)} | Nota 2")
        for indice in range(len(alunos)):
            aluno = alunos[indice]
    
            print(f"{indice+1}.{aluno["nome"].ljust(13)} | {str(aluno["nota1"]).ljust(8)} | {aluno["nota2"]}")



def consultar_medias():
    print("\n--- MÉDIAS E SITUAÇÕES ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            media = (aluno["nota1"] + aluno["nota2"]) / 2

            if media < 5:
                situacao = "Reprovado"
            elif media < 7:
                situacao = "Recuperação"
            else:
                situacao = "Aprovado"

            print(f"\nNome: {aluno['nome']}")
            print(f"Média: {media:.1f}")
            print(f"Situação: {situacao}")



while True:
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Consultar médias e situações")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        consultar_medias()

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")

