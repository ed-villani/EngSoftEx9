from unittest import TestCase
from ex1 import Fibonacci

class TestFibonacci(TestCase):
    def setUp(self):
        pass
    def test_rec(self):
        self.assertEqual(Fibonacci().rec(12), 144)


print(TestFibonacci().test_rec())
