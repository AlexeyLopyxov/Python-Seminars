import re

file_path = r'Phone_Number.txt'


def info_in_telephon_directory():
    print('Если хотите посмотреть всю информацию телефонного справочника введите: Al')
    print('Если хотите добавит контакт введите: Ad')
    print('Если хотите удалить контакт введите: D')
    print('Если хотите выполнить поиск по телефонной книге введите: S')
    print('Если хотите изменить телефонный справочник введите: C')

def all_info_in_telephon_directory():
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def added_more_contacts():
    with open(file_path, 'a', encoding='utf-8') as f:
        fio_name = input('Введите Фамилию Имя и Отчество: ')
        phone_number = input('Введите Телефон: ')
        f.write(fio_name + '\t')
        f.write(phone_number + '\n')
        print(f'\nКонтакт {fio_name} успешно добавлен!')


def delete_info_in_phone_number():
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()

    find_info = input('Введите ФИО контакта: ')
    pattern = re.compile(re.escape(find_info))
    with open(file_path, 'w', encoding='utf-8') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
    print(f'Контакт успешно удален!')


def search_info_in_phone_number():
    find_info = input('Введите поиск контакта: ')
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)


def change_info_in_phone_number():
    delete_info_in_phone_number()
    print('Добавьте заново контакт')
    added_more_contacts()
                

def input_info():
    info_in_telephon_directory()
    command_entered = str(input())
    if command_entered == 'Al':
        return (all_info_in_telephon_directory())
    elif command_entered == 'Ad':
        return (added_more_contacts())
    elif command_entered == 'D':
        print('Выберите из всего списка контакт, который хотите удалить: ')
        all_info_in_telephon_directory()
        return (delete_info_in_phone_number())
    elif command_entered == 'S':
        return (search_info_in_phone_number())
    elif command_entered == 'C':
        print('Выберите из всего списка контакт, который хотите изменить: ')
        all_info_in_telephon_directory()
        return (change_info_in_phone_number())
    else: print('Введите корректные данные!')

input_info()