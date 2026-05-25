class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            raise Exception("El libro ya está prestado")

        self.disponible = False

    def devolver(self):
        if self.disponible:
            raise Exception("El libro no estaba prestado")

        self.disponible = True