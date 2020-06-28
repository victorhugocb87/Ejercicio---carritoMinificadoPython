class estudiante():
    def __init__(self, e_nombre, e_apellido, e_carrera, e_materia):
        self.nombre = e_nombre
        self.apellido = e_apellido
        self.carrera = e_carrera
        self.materia = e_materia
    
    def saludar(self):
            return "Mi nombre es %s %s y estudio la carrera de %s"%(self.nombre, self.apellido, self.carrera)

    def materiaEstudiante(self):
            return "%s %s esta cursando la materia de %s"%(self.nombre, self.apellido, self.materia)

julio = estudiante("Julio", "Saucedo", "Ingenieria de Sistemas", "Programacion II")
maria = estudiante("Maria", "Mendoza", "Ingenieria de Comercial", "Matematicas")
jesica = estudiante("Jesica", "Vaca", "Contabilidad", "informatica Empresarial")

print("****************************")

print(julio.saludar())
print(maria.saludar())
print(jesica.saludar())

print("****************************")

print(julio.materiaEstudiante())
print(maria.materiaEstudiante())
print(jesica.materiaEstudiante())