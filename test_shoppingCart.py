from unittest import TestCase
from ex3 import ShoppingCart
from ex3 import Book

class TestShoppingCart(TestCase):
    def setUp(self):
        b1 = Book("a", "b", 2)
        b2 = Book("a2", "b2", 7)
        c = ShoppingCart()
        c.addBook(b1)
        c.addBook(b2)

    def test_addBook(self):
        self.assertEquals(ShoppingCart().addBook())

    def test_deleteCart(self):
        self.fail()

    def test_lenCart(self):
        self.fail()

    def test_valueCart(self):
        self.fail()

    def test_delBook(self):
        self.fail()
