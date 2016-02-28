# -*- coding: utf-8 -*-
"""Unit etsts for the 'addrmatch' module."""

import unittest

from uosc.addrmatch import addrmatch


class TestAddrmatch(unittest.TestCase):
    def test_empty_pattern_and_string(self):
        self.assertTrue(addrmatch('', ''))

    def test_single_char_pattern(self):
        self.assertTrue(addrmatch('?', 'a'))
        self.assertTrue(addrmatch('?', '0'))
        self.assertTrue(addrmatch('?', '.'))
        self.assertFalse(addrmatch('?', ','))
        self.assertFalse(addrmatch('?', '#'))
        self.assertFalse(addrmatch('?', '*'))
        self.assertFalse(addrmatch('?', '?'))
        self.assertFalse(addrmatch('?', '['))
        self.assertFalse(addrmatch('?', ']'))
        self.assertFalse(addrmatch('?', '{'))
        self.assertFalse(addrmatch('?', '}'))

    def test_multi_char_pattern(self):
        self.assertTrue(addrmatch('a*', 'a'))
        self.assertTrue(addrmatch('a*', 'aaa'))
        self.assertTrue(addrmatch('a*', 'abc'))
        self.assertFalse(addrmatch('a*', 'bbc'))
        self.assertTrue(addrmatch('*a', 'aaa'))
        self.assertTrue(addrmatch('*a', 'cba'))
        self.assertFalse(addrmatch('*a', 'cbc'))

    def test_pattern_longer_than_test(self):
        self.assertTrue(addrmatch('a**', 'a'))


if __name__ == '__main__':
    unittest.main()
