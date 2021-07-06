from func import *


def main():
    while True:
        command = input('\nВведите команду: ')
        if command == 'h':
            print(HELP)
        elif command == 'p':
            inp_number = str(input('Введите номер документа: '))
            owner = people(inp_number)
            print(f'\nВладелец документа: {owner}')
        elif command == 's':
            inp_number = str(input('Введите номер документа: '))
            shelf_num = shelf(inp_number)
            print(f'\nНомер полки: {shelf_num}')
        elif command == 'l':
            lst_docs()
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
            if doc_deleted:
                print(f'\nДокумент № {doc_num} удален!')
            else:
                print(f'Ошибка!')
        elif command == 'm':
            print(f'\n{directories}')
            doc_num = str(input('Введите номер документа: '))
            shelf_num = str(input('Введите номер целевой полки: '))
            print(move_doc(doc_num, shelf_num))
        elif command == 'as':
            print(f'\n{directories}')
            shelf_num = str(input('\nВведите номер новой полки: '))
            add_shelf(shelf_num)
        elif command == 'q':
            break
        else:
            print('Неправильная команда!')
            break


if __name__ == '__main__':
    main()
