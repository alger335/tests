# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит; s – shelf –
# команда, которая спросит номер документа и выведет номер полки, на которой он находится; Правильно обработайте
# ситуации, когда пользователь будет вводить несуществующий документ. l– list – команда, которая выведет список всех
# документов в формате passport "2207 876234" "Василий Гупкин"; a – add – команда, которая добавит новый документ в
# каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное
# название, передающие её действие.

# Задача №2. Дополнительная (не обязательная) d – delete – команда, которая спросит номер документа и удалит его из
# каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ; m – move –
# команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно
# обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на
# несуществующую полку; as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
# Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "52465465", "name": "Анатолий Вассерман"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': ['52465465']
}

HELP = '''
h - список команд.
p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
l – list – команда, которая выведет список всех документов
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и
номер полки, на котором он будет храниться.
d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. 
m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
q - выход
'''
print(HELP)


def people(inp_number):
    """p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
    """
    for document in documents:
        if inp_number == document["number"]:
            response = document["name"]
            return response
        else:
            response = False
    return response


def shelf(inp_number):
    """s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится
    """
    for key, value in directories.items():
        if inp_number in value:
            response = key
            return response
        else:
            response = False
    return response


def lst_docs():
    """l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    """
    for document in documents:
        print(f'{document["type"]} "{document["number"]}" "{document["name"]}"')


def add_doc(doc_type, doc_num, doc_own, shelf_num):
    """a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя
    владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет
    пытаться добавить документ на несуществующую полку.
    """
    doc_dict = {"type": doc_type, "number": doc_num,
                "name": doc_own}
    if shelf_num in directories.keys():
        directories[shelf_num].append(doc_dict["number"])
        documents.append(doc_dict)
        return shelf_num
    else:
        print('Нет такой полки!')
        shelf_add = str(input('Добавить новую полку? y/n: '))
        if shelf_add == 'n':
            print('Отмена')
        elif shelf_add == 'y':
            add_shelf(shelf_num)
            directories[shelf_num].append(doc_dict["number"])
            documents.append(doc_dict)
            print(f'\nДокумент добавлен на полку {shelf_num}')


def del_doc(doc_num):
    """ d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
    """
    for id, document in enumerate(documents):
        if doc_num == document["number"]:
            for key, value in directories.items():
                if doc_num in value:
                    directories[key].remove(doc_num)
            documents.pop(id)
            response = True
        else:
            response = False
    return response


def move_doc(doc_num, shelf_num):
    """m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    """
    for key, value in directories.items():
        if shelf_num in directories.keys():
            if doc_num in value:
                directories[key].remove(doc_num)
                directories[shelf_num].append(doc_num)
                response = True
                return response
            else:
                response = False
        else:
            response = False
    return response


def add_shelf(shelf_num):
    """as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда
    пользователь добавляет полку, которая уже существует.
    """
    if shelf_num not in directories.keys():
        directories.update({shelf_num: []})
        return True
    else:
        return False
