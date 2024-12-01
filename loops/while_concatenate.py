name = "Guilherme Galvão Kominami"

index = 0
new_name = ''
new_name2 = ''

while (index < len(name)):
    letter = name[index] 
    index += 1
    new_name += letter
    new_name2 += f'*{letter}'

print(new_name)
print(new_name2)
