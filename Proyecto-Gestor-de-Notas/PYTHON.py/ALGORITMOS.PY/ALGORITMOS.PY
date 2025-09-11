Notas = []

#lista global de notas
Notas = []
#PROCEDIMIENTO

#pide al usuario ingresar notas hasta que escribs fin que validaciones aplica
# no puede estar vacia
# debe ser numerica
# debe estar entre cero  y 100
def registrar_notas():
    while True:
        Entrada = input("Ingrese una nota (o escriba 'fin' para terminar): ").strip()
        if Entrada.upper() == "FIN":
            break
        if not Entrada.isdigit():
            print("Error: solo se permite ingresar valores numericos")
            continue

        Nota = int (Entrada)

        if Nota < 0 or Nota > 100:
            print("Error: la nota debe de estar dentro del rango de 0 y 100 ")
            continue

        Notas.append(Nota)
        print("SU nota fue ingresada con exito")

#FUNCION CALCULAR PROMEDIO
# Retrona el promedio de todas las notas en la lista 
# si no hay notas registradas devulve None
        
def Calcular_promedio(): 
    if len(Notas) == 0:
       return None 
    return sum(Notas)/ len(Notas)
        

#PROCEDIMIENTO
# recorre la lista y ceunta
# Aprovadas notas >= 60
# Reprobadas notas <60

def Contar_Aprobadas_y_Reprobadas():
    Aprobadas = sum(1 for n in Notas if n >= 60)
    Reprobadas = len(Notas) - Aprobadas  
    print (f"Cursos aprobados: {Aprobadas}")
    print(f"Cursos reprobados: {Reprobadas}")

#PROCEDIMIENTO BUSCAR NOTA
# permite buscar una nota en la lista usando BUSQUEDA LINEAL 
            
def Buscar_nota():
    buscar = input ("ingrese la nota que decea buscar: ")
    if buscar.isdigit():
       buscar = int(buscar)
       if buscar in Notas:
          print (f"La nota {buscar} fue encontrada en la lista")
       else: 
           print(f"La nota {buscar} no se encuentra registrada")
    else: 
        print(f"Busqueda cancelada : el valor no es numerico")


#PROCEDIMIENTO ACTUALIZAR NOTA
# permite modificar una nota usando su indice que es la posicion en la lista
# ejemplo para modificar la nota Notas[2] = 95
def Actualizar_nota():
    Actualizar = input("Desea actualizar alguna nota (si/no): ")

    if Actualizar.lower() == "si":
        indice = input(f"ingrese el indice de la nota a actualizar (0 a {len(Notas)-1}): ")
                    
        if indice.isdigit():
            indice = int(indice)89
            if 0 <= indice < len(Notas):
                nueva = input("ingrese la nota 0 a 100: " )
                if nueva.isdigit():
                   nueva = int(nueva)
                   if 0 <= nueva <= 100:
                     # aqui se modifica la nota DIRECTAMENTE EN LA LISTA
                      Notas[indice] = nueva
                      print("Nota actualizada con exito")
                   else: 
                       print("Error: la nota debe estar entre el rango 0 y 100")
                else: 
                    print("Error el valor ingresada no es numerico")
            else: 
                print("Error indice fuera de rango")
        else: 
            print("Error el indice debe ser un numero")
        

#eliminar notas de la lista usando su indice
def Eliminar_nota():
    if not Notas: #lista vacia
        print("NO HAY NOTAS REGISTRADAS PARA ELIMINAR")
        return
    
    indice = input(f"INGRESE EL INDICE DE LA NOTA A ELIMINAR (0 A {len(Notas)-1}): ")
    if indice.isdig():
        indice = int(indice)
        if 0 <= indice < len(Notas):
            eliminada = Notas.pop(indice)
            print(f"!!!NOTA ELIMINADA CON EXITO!!!: {eliminada}")
        else: 
            print("ERROR: INDICE FUERA DE RANGO")
    else: 
        print("ERROR: EL INDICE DEBE DE SER UN VALOR NUEMRICO")


#paso 1 registrar notas
registrar_notas()

#paso 2 calcular promedio
Promedio = Calcular_promedio()
if Promedio is None: 
    print ("No se puede calcular promedio porque no hay notas")
else: 
   print(f"El promedio de las notas es. {Promedio: .2f}")
#paso 3 contar aAprobados y Rprobados
Contar_Aprobadas_y_Reprobadas()

#paso 4 buscar nota 
Buscar_nota()

#paso 5 Actualizar nota
Actualizar_nota()
                  

def menu(): 
    while True:
        print("GESTOR DE NOTAS ACADEMICAS 2025")
        print("OPCIÒN 1. REGISTRAR NUEVO CURSO")
        print("OPCIÒN 2. MOSTRAR TODOS LOS CURSOS Y NOTAS")  
        print("OPCIÒN 3. CALCULAR PROMEDIO GENERAL")
        print("OPCIÒN 4. CONTAR CURSOS APROBADOS Y REPROBADOS")
        #Aqui se hace la busqueda linal en buscar curso por nombre
        print("OPCION 5. OPCIÒN 5. BUSCAR CURSOS POR NOMBRE")  
        print("OPCION 6. ACTUALIZAR NOTA POR INDICE")
        print("OPCION 7. ELIMINAR NOTA")
        print("OPCION 8. SALIR")
        opcion = input("seleccione una opc78FIion (1-7): ").strip()

        if opcion == "1":
            registrar_notas()
        elif opcion == "2":
            if Notas: 
                print ("NOTAS REGISTRADAS (con indices): ")
                for i, nota in enumerate(Notas):
                    print (f"[{i}]-> {nota}")
            else: 
                print("NO HAY NOTAS REGISTRADAS")
        elif opcion == "3": 
            promedio = Calcular_promedio()
            if promedio is None: 
                print("NO SE PUEDE CALCULAR PROMEDIO PORQUE NO HAY NOTAS")
            else:
                print(f"PROMEDIO GENERAL: {promedio: .2F}")
        elif opcion == "4":
              Contar_Aprobadas_y_Reprobadas()
        elif opcion == "5":
             Buscar_nota()
        elif opcion == "6": 
            Actualizar_nota()
        elif opcion == "7": 
            Eliminar_nota()
        elif opcion == "8":
            print("GRACIAS POR USAR EL GESTOR DE NOTAS. HASTA PRONTO.")
            break 
        else: 
            print("OPCION INVALIDA. INTENTE DE NUEVO (OPCION 1-8).").strip()


menu()
    




