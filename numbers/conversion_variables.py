"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

input_data = input("Digite um número inteiro:")

if input_data.isdigit():
    number = int(input_data)
    odd_even = number % 2 == 0
    odd_even_text = "ímpar"
    if odd_even:
        odd_even_text = "par"

    print(f"Número digitado {number} é {odd_even_text}")
else:
    print("Número não é inteiro.")    