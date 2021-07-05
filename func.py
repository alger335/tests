# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

# Задача №2. Дополнительная (не обязательная)
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

HELP = '''
h - список команд.
p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
l– list – команда, которая выведет список всех документов
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. 
m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
q - выход
'''
print(HELP)


def people(documents):
    '''p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
    '''
    inp_number = str(input('Введите номер документа: '))
    for document in documents:
        if inp_number == document["number"]:
            response = f'\nВладелец документа: {document["name"]}'
            return response
        else:
            response = 'Ошибка! Документ с таким номером отсутствует!'
    return response


def shelf(directories):
    '''s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится
    '''
    inp_number = input('Введите номер документа: ')
    for key, value in directories.items():
        if inp_number in value:
            response = f'\nНомер полки: {key}'
            return response
        else:
            response = 'Ошибка! Документ с таким номером отсутствует!'
    return response


def lst_docs(documents):
    '''l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    '''
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def add_doc(documents, directories):
    '''a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
    '''
    doc_dict = {}
    doc_dict["type"] = str(input('тип документа: '))
    doc_dict["number"] = str(input('номер документа: '))
    doc_dict["name"] = str(input('имя владельца: '))
    shelf_num = str(input('номер полки: '))
    if shelf_num in directories.keys():
        directories[shelf_num].append(doc_dict["number"])
        documents.append(doc_dict)
        print(f'\nДокумент добавлен на полку {shelf_num}')
    else:
        print('Неправильный номер полки!')


def del_doc(documents, directories):
    ''' d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
    '''
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')
    doc_num = str(input('\nВедите номер документа для удаления: '))
    for id, document in enumerate(documents):
        if doc_num == document["number"]:
            for key, value in directories.items():
                if doc_num in value:
                    directories[key].remove(doc_num)
            documents.pop(id)
            response = f'\nДокумент № {doc_num} удален!'
            return response
        else:
            response = '\nОшибка! Документ с таким номером отсутствует!'
    return response


def move_doc(directories):
    '''m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    '''
    print(f'\n{directories}')
    doc_num = str(input('Введите номер документа: '))
    shelf_num = str(input('Введите номер целоевой полки: '))
    for key, value in directories.items():
        if shelf_num in directories.keys():
            if doc_num in value:
                directories[key].remove(doc_num)
                directories[shelf_num].append(doc_num)
                response = f'\nДокумент № {doc_num} перемещен на полку {shelf_num}.'
                return response
            else:
                response = '\nОшибка! Документ с таким номером отсутствует!'
        else:
            response = '\nОшибка! Нет такой полки!'
    return response


def add_shelf(directories):
    '''as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.
    '''
    print(f'\n{directories}')
    shelf_num = str(input('\nВведите номер новой полки: '))
    if shelf_num not in directories.keys():
        directories.update({shelf_num: []})
        print(f'\nПолка {shelf_num} добавлена.')
    else:
        print(f'\nОшибка! Полка {shelf_num} уже существует')
    print(f'\n{directories}')


def main(documents, directories, HELP):
    while True:
        command = input('\nВведите команду: ')
        if command == 'h':
            print(HELP)
        elif command == 'p':
            print(people(documents))
        elif command == 's':
            print(shelf(directories))
        elif command == 'l':
            lst_docs(documents)
        elif command == 'a':
            add_doc(documents, directories)
        elif command == 'd':
            print(del_doc(documents, directories))
        elif command == 'm':
            print(move_doc(directories))
        elif command == 'as':
            add_shelf(directories)
        elif command == 'q':
            break
        else:
            print('Неправильная команда!')
            break


main(documents, directories, HELP)