from libro import Libro
from miembro import Miembro
from biblioteca import Biblioteca

biblioteca = Biblioteca()

libro1 = Libro("Python Básico", "Juan Pérez", "123")
miembro1 = Miembro("Evelyn", "45678912")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_miembro(miembro1)

try:
    miembro1.prestar_libro(libro1)
    print("Libro prestado correctamente")

    miembro1.prestar_libro(libro1)

except Exception as e:
    print("Error:", e)

biblioteca.mostrar_libros()