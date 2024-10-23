import os

BASE_DIR = 'Base'
LIST_BASE = []

def searchBase():
    global LIST_BASE
    for base_file in os.listdir(BASE_DIR):LIST_BASE+=[base_file]

def selectBase():
    global LIST_BASE
    
    searchBase()

    number_base = 0
    for base in LIST_BASE:
        number_base+=1
        print(f'[{number_base}] {base}')
    print('')

    selectNumber = int(input('Выберите базу: '))
    selectNumber-=1
    try:
        target = f'{BASE_DIR}/{LIST_BASE[selectNumber]}'
        return target
    except IndexError as err:print(f'Некорректный выбор: {err}')
    except Exception as err:print(f'Error: {err}')
