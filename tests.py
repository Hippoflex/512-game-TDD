import unittest

from logics import *


class Test_512(unittest.TestCase):
    def test_number_from_index_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_number_from_index_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_empty_list_1(self):
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(empty_list(mas), a)

    def test_empty_list_2(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

        a = [9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(empty_list(mas), a)

    def test_empty_list_3(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]

        a = []
        self.assertEqual(empty_list(mas), a)

    def test_get_index_from_number_1(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_get_index_from_number_2(self):
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_get_index_from_number_3(self):
        self.assertEqual(get_index_from_number(5), (1, 0))
