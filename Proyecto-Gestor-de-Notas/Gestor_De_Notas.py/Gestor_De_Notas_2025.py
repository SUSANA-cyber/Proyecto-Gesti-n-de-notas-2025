 
 
 #Lista para guardar los cursos y notas
#Registro de notas y cursos
Cursos = []

#Procedimiento que pide al usuario el nombre y la nota de un curso y lo guarda en la lista de cursos
def RegistrarCurso():
    Nombre = input ("Ingrese el nombre del Curso ")
    Nota = int(input("ingrese la nota del curso (0 a 100): "))
    #Agregamos un diccionario con los datos a la lista 
    Cursos.append({"Nombre": Nombre, "Nota": Nota})

    print("Curso Guardado con exito!!!")

#Bucle para registrar varios curosos 
while True:
    RegistrarCurso()
    #Preguntar si quiere agregar otro curso
    Opcion = input ("Desea agregar otro curso (SI/NO): ")
    if Opcion != 'SI':
        #si opcion es distinto que si sale del bucle
        break
#se muestra todos los cursos registrados
print ("Lista de cursos registrados: ")
for Curso in Cursos:
    print (f"Curso: {Curso['Nombre']}, Nota: {Curso['Nota']}")







