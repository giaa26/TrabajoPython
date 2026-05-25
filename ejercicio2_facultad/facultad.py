class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.profesores = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)