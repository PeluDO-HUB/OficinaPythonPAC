"""
1. Conversor de temperatura
Crie uma função chamada converter_temperatura()
que receba uma temperatura em Celsius e retorne o valor convertido para Fahrenheit
e Kelvin
Fórmula: 
Fahrenheit = Celsius × 1,8 + 32.
Kelvin = Celsius + 273.15
No programa principal, peça a temperatura ao usuário e mostre o resultado.
"""




def converter_temperatura(temp):
    fh = temp * 1.8 + 32
    kelvin = temp +273.15
    print(f"a temperatura de {temp}°C é igual a {fh}°F")
    print(f"que é igual á {kelvin}°K")


def converter_temperaturav2(temp, inicio, convertido):
    while True:
        inicio = inicio.lower()
        convertido = convertido.lower()

        if inicio not in ["c", "celsius", "k", "kelvin", "f", "fahrenheit"]:
            print("Tipo de temperatura inicial inválido!")
            inicio = input(
                "Insira a temperatura inicial: "
                "c=Celsius k=Kelvin f=Fahrenheit\n"
            )
            continue

        elif convertido not in ["c", "celsius", "k", "kelvin", "f", "fahrenheit"]:
            print("Tipo de conversão incorreto!")
            convertido = input(
                "Insira para qual converter: "
                "c=Celsius k=Kelvin f=Fahrenheit\n"
            )
            continue

        if inicio in ["c", "celsius"]:
            if convertido in ["f", "fahrenheit"]:
                valorConvert = temp * 1.8 + 32
            elif convertido in ["k", "kelvin"]:
                valorConvert = temp + 273.15
            else:
                valorConvert = temp

        elif inicio in ["k", "kelvin"]:
            if convertido in ["c", "celsius"]:
                valorConvert = temp - 273.15
            elif convertido in ["f", "fahrenheit"]:
                valorConvert = (temp - 273.15) * 1.8 + 32
            else:
                valorConvert = temp

        else:
            if convertido in ["c", "celsius"]:
                valorConvert = (temp - 32) / 1.8
            elif convertido in ["k", "kelvin"]:
                valorConvert = (temp - 32) / 1.8 + 273.15
            else:
                valorConvert = temp

        if inicio in ["c", "celsius"]:
            inicio = "Celsius"
        elif inicio in ["k", "kelvin"]:
            inicio = "Kelvin"
        else:
            inicio = "Fahrenheit"

        if convertido in ["c", "celsius"]:
            convertido = "Celsius"
        elif convertido in ["k", "kelvin"]:
            convertido = "Kelvin"
        else:
            convertido = "Fahrenheit"

        print(
            f"A temperatura {inicio} de {temp:.2f}°{inicio[0]} "
            f"convertida em {convertido} é de "
            f"{valorConvert:.2f}°{convertido[0]}"
        )
        break


"""while True:
    try:
        temp = float(input("Insira a temperatura para convertê-la: "))
        break
    except ValueError:
        print("Valor inválido. Insira uma temperatura numérica.")
inicio = input("Insira o tipo de temperatura\n c=Celsius k=Kelvin f=Fahrenheit\n")
fim = input("Agora insira para qual temperatura quer converter\n c=Celsius k=Kelvin f=Fahrenheit\n ")
#converter_temperatura(celsius)
converter_temperaturav2(temp,inicio,fim)"""

"""
crie uma função converter_temperatura() que receba a temperatura, 
a unidade de origem e a unidade de destino 
e utilize as outras funções para realizar a conversão.
"""

"""
1. Calculadora de viagem
Crie uma função chamada calcular_combustivel() que receba a distância de uma viagem, 
o consumo do veículo em km/L e o preço do litro do combustível.
A função deve calcular e retornar a quantidade de litros necessária para a viagem 
e o custo total estimado.
Exemplo:
- Distância: 300 km
- Consumo: 10 km/L
- Preço do litro: R$ 6,00
- Resultado: 30 litros e R$ 180,00.
"""

def calcular_combustivel():
    while True:
        try:
            km = float(input("Digite a distância a ser percorrido em Km: "))
            continue
        except ValueError:
            print("Valor inserido incorreto, tente novamente!")

        try:
            consumo = float(input("Digite o consumo Km/L "))
            continue
        except ValueError:
             print("Valor inserido incorreto, tente novamente!")

        try:
            preco = float(input("Digite o valor do Litro "))
            continue
        except ValueError:
            print("Valor inserido incorreto, tente novamente!")

        print(f"A distância percorrida será de {km:.1f}KM, com o valor do litro de {preco:.2f} "
              f"e consumo do veiculo de {consumo:.1f}KM/L")
        print(f"O valor gastado nessa viagem será de R${preco*consumo}")
        
                                  

    
 
"""
2. Máquina de lanches
Crie uma função chamada calcular_troco() que receba o preço de um lanche 
e o valor pago pelo cliente.
A função deve retornar o troco. Caso o valor pago seja insuficiente, 
deve informar quanto falta para completar o pagamento.
Exemplo:
- Preço do lanche: R$ 18,50
- Valor pago: R$ 20,00
- Resultado: R$ 1,50 de troco.
"""

def calcular_troco(precoLanche,pago):
    if precoLanche>pago:
        print(f"O cliente está devendo R${(precoLanche-pago):.2f}")
    elif precoLanche==pago:
        print(f"Foi pago o valor exato!")
    else:
        print(f"O cliente deve receber R${(pago-precoLanche):.2f}")




"""
3. Simulador de XP
Em um jogo, o personagem sobe de nível conforme ganha experiência.

Crie uma função chamada calcular_nivel() que receba a quantidade de 
XP do jogador e retorne o nível correspondente, seguindo as regras:
- Menos de 100 XP: nível 1.
- De 100 a 299 XP: nível 2.
- De 300 a 599 XP: nível 3.
- 600 XP ou mais: nível 4.
No programa principal, solicite o XP do jogador e 
exiba o nível retornado pela função.
"""
expAcumulado = 0
def calcularNivel(xp):
    expAcumulado+=xp
    if expAcumulado<100:
        print(f"Você possui {expAcumulado} expêriencia acumulada e se " 
              "encontra no nivel 1")
    elif expAcumulado>=100 and expAcumulado<300:
        print(f"Você possui {expAcumulado} expêriencia acumulada e se " 
                      "encontra no nivel 2")
    elif expAcumulado>=300 and expAcumulado <500:
        print(f"Você possui {expAcumulado} expêriencia acumulada e se " 
                      "encontra no nivel 3")
    elif expAcumulado>=500:
        print(f"Você possui {expAcumulado} expêriencia acumulada e se " 
                      "encontra no nivel 5, o Nivel máximo :)")

        

""" 
4. Simulador de compra parcelada
Crie uma função chamada calcular_parcela() que receba o preço de um produto 
e a quantidade de parcelas desejada.
Regras:
- Pagamento à vista (1 parcela): desconto de 10%.
- De 2 a 3 parcelas: sem desconto ou acréscimo.
- Acima de 3 parcelas: acréscimo de 10% sobre o preço original.
A função deve retornar o valor de cada parcela.
"""
def calcular_parcela(produto,parcela):
    if parcela == 1:
        print(f"O valor a ser pago vai ser de R${produto*0.9}")
    elif parcela > 1 and parcela<=3:
        print(f"O valor a ser pago vai ser de R${produto}, Sem descontos.")
    elif parcela>3:
        print(f"O valor a ser pago vai ser de R${produto*1}")
    else:
        print(f"Valor informado de parcela invalido tente novamente")

    

calcular_parcela(300,0)
"""
5. Desafio — Conversor de temperaturas
Crie uma função chamada converter_temperatura() que receba três parâmetros:
- temp: valor da temperatura.
- inicio: unidade de origem da temperatura.
- convertido: unidade para a qual deseja converter.
A função deve realizar a conversão entre Celsius, Fahrenheit e Kelvin e exibir o resultado.

O usuário poderá informar as unidades utilizando a letra inicial ou o nome completo, por exemplo: c ou celsius, f ou fahrenheit, k ou kelvin.

Fórmulas disponíveis:
Conversão	Fórmula
Celsius → Fahrenheit	F = C x 1,8 + 32
Celsius → Kelvin	K = C + 273,15
Fahrenheit → Celsius	C = (F - 32) / 1,8
Fahrenheit → Kelvin	K = (F - 32) / 1,8 + 273,15
Kelvin → Celsius	C = K - 273,15
Kelvin → Fahrenheit	F = (K - 273,15) x 1,8 + 32"""


"""
def menu():
    while True:
        print("Escolha a atividade a ser iniciada digitando o numero:")
        print("1. Conversor de Temperatura")
        print("2. Calcular Troco")
        print("3. Experiencia de Nivel")
        print("4. Calcular Parcelas")
        escolha = int(input("Digite a opção: "))
        if escolha == 1:
            while True:
                print("Escolha qual versão deseja testar: ")
                print("1. Simples ou 2. Desafio")
                escolha = int(input("Digite a opção: "))
                if escolha == 1:

                    converter_temperatura(temp)
                elif escolha==2:

                    converter_temperaturav2(temp,inicio,fim)
        elif escolha == 2:

            calcular_troco(total,pago)
        elif escolha == 3:

            calcularNivel(xp)
        elif escolha== 4:

            calcular_parcela(total,qtdParcela)"""
         



