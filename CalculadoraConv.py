#Conversão de inputs
texto = str(input("Digite um texto: "))
numero_inteiro = int(input("Digite um número inteiro: ")) 
numero_decimal = float(input("Digite um número decimal: "))


"""
Peça ao usuário para digitar dois números e exiba
a soma, subtração, multiplicação e divisão desses números.
"""
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f"A soma de {numero1} e {numero2} é: {soma:.2f}")
print(f"A subtração de {numero1} e {numero2} é: {subtracao:.2f}")
print(f"A multiplicação de {numero1} e {numero2} é: {multiplicacao:.2f}")
print(f"A divisão de {numero1} e {numero2} é: {divisao:.2f}")
