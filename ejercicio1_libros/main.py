from libro import Libro
from miembro import Miembro
from biblioteca import Biblioteca

biblioteca = Biblioteca()

libro1 = Libro("Harry Potter", "J.K Rowling", "111")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "222")

miembro1 = Miembro("Evelyn", "12345678")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.agregar_miembro(miembro1)

try:
    miembro1.prestar_libro(libro1)

except Exception as e:
    print("Error:", e)

biblioteca.mostrar_libros()
biblioteca.mostrar_miembros()