class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def mostrar_libros(self):
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"{libro.titulo} - {estado}")