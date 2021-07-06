from func import *


def main():
    while True:
        command = input('\nВведите команду: ')
        if command == 'h':
            print(HELP)
        elif command == 'p':
            inp_number = str(input('Введите номер документа: '))
            owner = people(inp_number)
            if not owner:
                print('Ошибка')
            else:
                print(f'\nВладелец документа: {owner}')
        elif command == 's':
            inp_number = str(input('Введите номер документа: '))
            shelf_num = shelf(inp_number)
            if not shelf_num:
                print('Ошибка!')
            else:
                print(f'\nНомер полки: {shelf_num}')
        elif command == 'l':
            for document in lst_docs():
                print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')
        elif command == 'a':
            doc_type = str(input('Введите тип документа: '))
            doc_num = str(input('Введите номер документа: '))
            doc_own = str(input('Введите имя владельца: '))
            shelf_num = str(input('Введите номер полки: '))
            doc_added = add_doc(doc_type, doc_num, doc_own, shelf_num)
            print(f'\nДокумент добавлен на полку {doc_added}')
        elif command == 'd':
            for document in documents:
                print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')
            doc_num = str(input('\nВедите номер документа для удаления: '))
            doc_deleted = del_doc(doc_num)
            print(doc_deleted)
            if doc_deleted:
                print(f'\nДокумент № {doc_num} удален!')
            else:
                print(f'Ошибка!')
        elif command == 'm':
            print(f'\n{directories}')
            doc_num = str(input('Введите номер документа: '))
            shelf_num = str(input('Введите номер целевой полки: '))
            doc_moved = move_doc(doc_num, shelf_num)
            if doc_moved:
                print(f'Документ {doc_num} перемещен на полку {shelf_num}!')
            else:
                print(f'\nОшибка!')
        elif command == 'as':
            print(f'\n{directories}')
            shelf_num = str(input('\nВведите номер новой полки: '))
            if add_shelf(shelf_num):
                print(f'\nПолка {shelf_num} добавлена.')
            else:
                print(f'\nОшибка! Полка {shelf_num} уже существует')

        elif command == 'q':
            break
        else:
            print('Неправильная команда!')
            break


if __name__ == '__main__':
    main()
