class Book:
    def __init__(self, titulo, isbn, preco):
        self.__titulo = titulo
        self.__isbn = isbn
        self.__preco = preco

    # get
    def getTitulo(self):
        return self.__titulo

    def getISBN(self):
        return self.__isbn

    def getPreco(self):
        return self.__preco

    # set
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setISBN(self, isbn):
        self.__isbn = isbn

    def setPreco(self, preco):
        self.__preco = preco


class ShoppingCart:
    def __init__(self):
        self.__books = []

    def addBook(self, book):
        self.__books.append(book)
        return 1

    def deleteCart(self):
        self.__books.clear()
        return 1

    def lenCart(self):
        return len(self.__books)

    def valueCart(self):
        soma = 0
        livros = self.__books
        for i in range(len(livros)):
            soma += livros[i].getPreco()
        return soma
    def delBook(self, isbn):
        livros = self.__books
        for i in range(len(livros)):
            if livros[i].getISBN() == isbn:
                livros.pop(i)
                return 1
        return 0
