#include <stdlib.h>
import os

shop_list = ['beans', 'beer', 'pasta', 'salsa', 'joe']

def list_items():
    for item_index, item_description in enumerate(shop_list):
        print(item_index, item_description)

while True:
    list_options = input('Select an option: [i]nsert [d]elete [l]ist: ')
    
    if list_options == 'i':
        list_item_added = input('Type an item: ')  
        shop_list.append(list_item_added)
        list_items()


    elif list_options == 'l':
        list_items()

    elif list_options == 'd':
        list_items()
        list_item_delete = int(input('Type the list number: '))

        try:
            indice = int(list_item_delete)
            del shop_list[indice]
            list_items()            
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')            

    else:
        print('Option invalid.')             