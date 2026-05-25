class Estudiante:
    def __init__(self, nombre, dni):
        if nombre == "":
            raise Exception("El nombre no puede estar vacío")

        self.nombre = nombre
        self.dni = dni