import task4
import unittest
from unittest import TestCase


class TestTask4(TestCase):
    def setUp(self):
        """Init"""

    def test_is_list_type(self):
        """Test for is _list_type"""
        self.assertTrue(type(task4.f(17)) == list)
        self.assertFalse(type(task4.f(17)) != list)

    def test_is_correct_len(self):
        """Test for is _correct_len"""
        self.assertTrue(len(task4.f(17)) == 17)
        self.assertFalse(len(task4.f(17)) != 17)

    def test_is_correct_dec_value(self):
        """Test for is _correct_dec_val"""
        self.assertTrue(int(task4.f(17)[16][0]) == 17)
        self.assertFalse(int(task4.f(17)[16][0]) != 17)

    def tearDown(self):
        """Finish"""


if __name__ == '__main__':
    unittest.main()
