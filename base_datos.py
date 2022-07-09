# Importación de librerías y módulos
from collections import namedtuple


# Función para crear una base de datos de estudiantes en una tupla nombrada
def base_datos_estudiantes():

  lista_estudiantes = []
  estudiante = namedtuple("estudiante", "nombre apellido edad ciclo")

  estudiante1 = estudiante("Andrea", "Campo", 26, "1")
  estudiante2 = estudiante("Nicolás", "Barrios", 32, "1")
  estudiante3 = estudiante("Johny", "Marin", 23, "2")

  lista_estudiantes.append(estudiante1)
  lista_estudiantes.append(estudiante2)
  lista_estudiantes.append(estudiante3)

  return lista_estudiantes