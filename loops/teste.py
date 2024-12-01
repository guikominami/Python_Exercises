"""
https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34610778#overview

Faça um jogo para o usuário adivinhar qual
a palavra secreta.

- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.

Faça a contagem de tentativas do seu
usuário.
"""

while True:

    try:
        letter_typed = input("Type a letter.")
        if len(letter_typed) > 1:
            print("Type just one letter.")
            continue


    except SystemError as error:
        print("erro")
