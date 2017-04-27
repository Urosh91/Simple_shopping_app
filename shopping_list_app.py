import os

shop_list = []


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_help():
    print('What do you want to pick up at the store?')
    print('''
Enter "Done" or "Quit" to stop adding items.
Enter "Help" for help.
Enter "Show" to see current state of your list.
Enter "Remove" to delete an item from your list.
''')


def show_list():
    clear()
    print('This is your list:')
    for index, item in enumerate(shop_list):
        print(f'{index+1}. {item}')

    print('-'*10)


def add_item(new_item):
    show_list()
    if shop_list:
        position = input(f'Where should I add {new_item}\n'
                         'Press ENTER to add to the end of the list\n'
                         '> ')
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shop_list.insert(position-1, new_item)
    else:
        shop_list.append(new_item)
    show_list()


def remove_from_list():
    show_list()
    what_to_remove = input('What would you like to remove?\n> ')
    try:
        shop_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

show_help()
while True:
    new_item = input('> ')

    if new_item.lower() == 'done' or new_item.lower() == 'quit':
        break
    elif new_item.lower() == 'help':
        show_help()
    elif new_item.lower() == 'show':
        show_list()
    elif new_item.lower() == 'remove':
        remove_from_list()
    else:
        add_item(new_item)


show_list()
