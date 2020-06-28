class RegistroMateria:
    def __init__(self, p_estudiante, p_apellido, p_carrera):
        self.estudiante = p_estudiante
        self.apellido = p_apellido
        self.carrera = p_carrera
        self.materias = []
    def presentarse(self):
        print("***************Presentacion de {} {}****************".format(self.estudiante, self.apellido))
        for i in self.materias:
            print(i)
        return "Soy el Estudiante: {} de la carrera de {}".format(self.estudiante, self.carrera)
    def registrarMateria(self):
        print("Gestion de registro de materias")
        materia = input('Digite las materias:')
        self.materias.append(materia)
        print("Materia {} registrada exitosamente.!".format(materia))
        adicional = input("Desea registrar una materia adicional?: y/n: ")
        if (adicional == 'y'):
            self.registrarMateria()
        else:
            return "Materia Registrada exitosamente.!!"
    def menu(self):
        opciones = """
        Menu de la aplicacion
        1.- Registrar Materias 
        2.- Presentarse
                    """
        print(opciones)
        eleccion = int(input('Elija una opcion:'))
        if(eleccion == 1):
            print(self.registrarMateria())
            self.menu()
        elif(eleccion == 2):
            print(self.presentarse())
            self.menu()
        else:
            print("Elija una opcion del menu")
            self.menu()

pedro = RegistroMateria("Pedro", "Perez", "Ingenieria de Sistemas")
pablo = RegistroMateria("Pablo", "Mercado", "Ingenieria Comercial")
print(pedro.menu())


