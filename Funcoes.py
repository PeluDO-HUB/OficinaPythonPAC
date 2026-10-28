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
    fh =  (temp * 1.8) + 32
    kelvin = temp + 273.15
    print (f"A temperatura de {temp}°C.")
    print(f"Em Fahrenheit é igual {fh}°F")
    print(f"Em Kelvin é igual {kelvin}°K")




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

        if convertido not in ["c", "celsius", "k", "kelvin", "f", "fahrenheit"]:
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


temp = float(input("Insira a temperatura em para converte-la: "))
inicio = input("Insira o tipo de temperatura\n c=Celsius k=Kelvin f=Fahrenheit\n")
fim = input("Agora insira para qual temperatura quer converter\n c=Celsius k=Kelvin f=Fahrenheit\n ")
#converter_temperatura(celsius)
converter_temperaturav2(temp,inicio,fim)

"""
crie uma função converter_temperatura() que receba a temperatura, 
a unidade de origem e a unidade de destino 
e utilize as outras funções para realizar a conversão.
"""





