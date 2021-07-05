from func import *
# from test_yandex import *
import unittest
class TestApp(unittest.TestCase):
    def test_doc_num(self):
        self.assertEqual("Василий Гупкин", get_doc_owner_name("2207 876234"))
    # def test_show_info_test(self):
    #     self.assertEqual('passport "2207 876234" "Василий Гупкин"', show_document_info(document))
    # def test_add_info(self):
    #     self.assertEqual('1', add_new_doc(new_num,new_doc_owner,new_type,new_doc_shelf))
    # def test_delete_info(self):
    #     self.assertEqual(('11-2', True), delete_doc('11-2'))
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