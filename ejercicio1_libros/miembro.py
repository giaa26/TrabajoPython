class Miembro:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = []

    def prestar_libro(self, libro):
        libro.prestar()
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        libro.devolver()
        self.libros_prestados.remove(libro)