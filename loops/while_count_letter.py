phrase = 'Python é uma linguagem de programação de alto nível, ' \
        'interpretada de script, imperativa, orientada a objetos.' \

counter = 1 
letter_more = ''
letter_times = 0

while counter < len(phrase):
    letter = phrase[counter]
    
    if letter.replace(' ', '') == '':
        counter+=1 
        continue
    
    letter_times_actual = phrase.count(letter)

    if letter_times < letter_times_actual:
        letter_times = letter_times_actual
        letter_more = letter

    #print(letter, letter_times_actual)
    counter+=1 

print(f'Letter that appeared most: {letter_more}')