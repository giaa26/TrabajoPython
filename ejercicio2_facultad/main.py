from estudiante import Estudiante
from profesor import Profesor
from facultad import Facultad

facultad = Facultad()

try:
    estudiante1 = Estudiante("Evelyn", "12345678")
    profesor1 = Profesor("Carlos", "Programación")

    facultad.agregar_estudiante(estudiante1)
    facultad.agregar_profesor(profesor1)

    facultad.mostrar_estudiantes()

except Exception as e:
    print("Error:", e)