from unittest import TestCase
from ex3 import ShoppingCart
from ex3 import Book
#q
class TestShoppingCart(TestCase):
    def setUp(self):
        self.b1 = Book("a", "b", 2)
        self.b2 = Book("a2", "b2", 7)
        self.c = ShoppingCart()
        self.c.addBook(self.b1)
        self.c.addBook(self.b2)

    def test_addBook(self):
        self.assertEqual(ShoppingCart().addBook(self.b1), 1)

    def test_deleteCart(self):
        self.assertEqual(ShoppingCart().deleteCart(), 1)

    def test_lenCart(self):
        self.assertEqual(self.c.lenCart(), 2)

    def test_valueCart(self):
        self.assertEqual(self.c.valueCart(), 9)

    def test_delBook(self):
        self.assertEqual(self.c.delBook(self.b1.getISBN()), 1)
