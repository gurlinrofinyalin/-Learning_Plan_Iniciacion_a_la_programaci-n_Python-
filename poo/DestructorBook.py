class Book():
    """
    Clase para trabajar con libros
    """
    def __init__(self, title, author = "", electronic = False):
        self.title = title
        self.author = author
        self.is_electronic = electronic
    def __del__(self):
        print("Acabas de llamar al métododestructor. El objeto acaba de ser eliminado")



#Para eliminar un objeto, utilizaos la palabra reservada del
book = Book("Lazarillo de Tormes")
print(book.title)
del book