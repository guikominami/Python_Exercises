list_example = [123, 456, 789, 101]
print(list_example[2])
print(list_example)

#delete the item in the index
del list_example[2]
print(f'delete the third item in the list: {list_example}')

#add a item in the last index in the list
list_example.append(888)
print(f'add a item in the last index: {list_example}')

#delete the last value
list_example.pop()
print(f'delete the last value: {list_example}')

#insert in the index in the first parameter
list_example.insert(2, 333)
print(f'insert in the index 2: {list_example}')

#Concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(f'lists added: {list3}')

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f'list extended: {list1}')

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2.extend(list1)
print(f'list extended inverted: {list2}')

list_names = ['João', 'Maria', 'Lara', 'Otto']
for name in list_names:
    print(name, type(name))

list_numbers = enumerate(list_names) 
print('list numbers')
for name in list_numbers:
    print(name)