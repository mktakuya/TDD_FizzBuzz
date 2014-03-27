#!/usr/bin/env python
# coding:utf-8
import unittest
from fizzbuzz import fizz_buzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz_3(self):
        actual = fizz_buzz('3')
        self.assertEqual("Fizz", actual)

    def test_fizzbuzz_5(self):
        actual = fizz_buzz('5')
        self.assertEqual("Buzz", actual)

    def test_fizzbuzz_7(self):
        actual = fizz_buzz('7')
        self.assertEqual('7', actual)

    def test_fizzbuzz_15(self):
        actual = fizz_buzz('15')
        self.assertEqual("FizzBuzz", actual)

    def test_fizzbuzz_a(self):
        actual = fizz_buzz('a')
        self.assertEqual('a', actual)

if __name__ == '__main__':
    unittest.main()

