from func import *
# from test_yandex import *
import unittest


class TestShelfAppUnitTest(unittest.TestCase):
    def test_people(self):
        self.assertEqual("Василий Гупкин", people("2207 876234"))

    def test_shelf(self):
        self.assertEqual("2", shelf("10006"))

    # def test_lst_docs(self):
    #     self.assertEqual("1", shelf("11-2"))

    def test_add_doc(self):
        self.assertEqual("3", add_doc("test_type", "1234", "Виталий Иванов", "3"))

    def test_del_doc(self):
        del_doc("52465465")
        self.assertEqual(False, shelf("52465465"))
        self.assertEqual(False, people("52465465"))

    def test_move_doc(self):
        move_doc("11-2", "2")
        self.assertEqual("2", shelf("11-2"))

    def test_add_shelf(self):
        self.assertEqual(True, add_shelf("6"))
        self.assertEqual(False, add_shelf("2"))

    # def test_yandex_success(self):
    #     self.assertEqual(201, ya.upload_folder_to_disk('test'))
    # def test_yandex_check(self):
    #     json = ya.get_files_list()
    #     json_data = json['_embedded']['items']
    #     list = []
    #     for dict in json_data:
    #         for key in dict.items():
    #             for item in key:
    #                 list.append(item)
    #     print(list)
    #     self.assertIn('papka19', list)
