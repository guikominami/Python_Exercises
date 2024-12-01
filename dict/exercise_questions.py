#include <stdlib.h>
import os

question_data = [
    {
        'Question': '2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': '5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': '10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

os.system('cls')

qt_right = 0
for question in question_data:

    print(question, type(question))

    print('Question: ', question['Question'])
    print()

    options = question['Options']

    for index, option in enumerate(options):
        print(f'{index}) {option}')

    print()

    answer_typed = input('Type the answer: ')

    right_answer = False
    anser_typed_int = None
    qt_options = len(options)   

    if answer_typed.isdigit():
        answer_typed_int = int(answer_typed)     

    if answer_typed_int is not None:
        if answer_typed_int >= 0 and answer_typed_int < qt_options:
            if options[answer_typed_int] == question['Answer']:
                right_answer = True    


    print()
    if right_answer:
        qt_right += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


    print('Você acertou', qt_right)
    print('de', len(question), 'perguntas.')
    

