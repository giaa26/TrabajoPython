class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def mostrar_libros(self):
        print("\nLISTA DE LIBROS")

        for libro in self.libros:

            if libro.disponible:
                estado = "Disponible"
            else:
                estado = "Prestado"

            print(f"""
Título: {libro.titulo}
Autor: {libro.autor}
ISBN: {libro.isbn}
Estado: {estado}
""")

    def mostrar_miembros(self):
        print("\nLISTA DE MIEMBROS")

        for miembro in self.miembros:

            print(f"""
Nombre: {miembro.nombre}
DNI: {miembro.dni}
""")