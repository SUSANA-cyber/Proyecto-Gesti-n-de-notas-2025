Notas = []

#lista donde se guardan los cursos + las notas 
#cada elemento de la lista es un diccionario por ejemplo curso: algoritmos, nota 77
#un diccionario un diccionario almacena cualquier tipo de dato 
cursos = []
#PROCEDIMIENTO

# funcion registrar curso

#pide al usuario ingresar el nombre de un curso y su nota
#hace validaciones: no vacio, valores numericos entre 0 y 100
#guarda curso dentro de la lista llamada cursos

def registrar_cursos():
    while True:
        nombre = input("INGRESE EL NOMBRE DEL CURSO QUE DECEA REGISTRAR (O ESCRIBA 'FIN' PARA TERMINAR): ").strip()
        
        #si el usuario escribe FIN deja de registrar cursos
        if nombre.upper() == "FIN":
            break

        #validaciones el nombre no puede estar vacio

        if nombre == "":
            print("ERROR: EL NOMBRE NO PUEDE ESTAR VACIO")
            continue
        #pediomos la nota

        nota = input("INGRESE LA NOTA DEL CURSO (0 A 100): ").strip()
        
        #la nota debe ser numerica

        if not nota.isdigit():
            print("Error: solo se permite ingresar valores numericos")
            continue
        #convierte la nota en numeros enteros
        nota = int (nota)

        if nota < 0 or nota > 100:
            print("Error: la nota debe de estar dentro del rango de 0 A 100 ")
            continue
        #guarda cursos + notas en un diccionario
        cursos.append({"curso": nombre, "nota": nota})
        print(f"curso '{nombre}' REGISTRADO CON EXITO!!!")

#FUNCION MOSTRAR CURSO
#recorre la lista de cursos y muestra el nombre del curso y la nota
#y si no hay curso se lo dice al usuario

def mostrar_curso():
    if cursos: 
        print("CURSOS REGISTRADOS (CON INDICE): ")
        #enumera da indice + el elemento
        for i, item in enumerate(cursos):
            print(f"[{i}] -> {item['curso']} - Notas: {item['nota']}") 
    else: 
        print("LO SIENTO NO HAY CURSOS REGISTRADOS.")

#FUNCION CALCULAR PROMEDIO
# Retrona el promedio de todas las notas registradas en la lista 
# si no hay notas registradas devulve None
        
def Calcular_promedio(): 
    if len(cursos) == 0:
       return None 
    #aqui recorre todos los cursos y suma sus notas 
    return sum(item["nota"] for item in cursos) / len(cursos)
        

#PROCEDIMIENTO
# recorre todos los cursos y cuentas cuantos estan aprobados
# Aprovadas notas >= 60
# Reprobadas notas < 60

def Contar_Aprobadas_y_Reprobadas():
    Aprobadas = sum(1 for item in cursos if item["nota"] >= 60)
    Reprobadas = len(cursos) - Aprobadas  
    print (f"Cursos aprobados: {Aprobadas}")
    print(f"Cursos reprobados: {Reprobadas}")

#PROCEDIMIENTO BUSCAR NOTA LINEAL
#AQUI SE USA LA BUSQUEDA LINEAL EN LA LISTA CURSOS
# LE PIDE AL USUARIO UN NOMBRE DE CURSO Y BUSCA COINCIDENCIAS
#SI ESCRIBE ALGO ENCUENTRA ALGORITMOS
            
def Buscar_curso():
    nombre = input ("INGRESE EL NOMBRE DEL CURSO QUE BUSCA: ").strip().lower()
    #VALIDACION si el usuario no ingreso nada avisamos y sale 
    if nombre == "":
        print("DEBE DE INGRESAR UN NOMBRE PARA REALIZAR LA BUSQUEDA.")
        #sale de la funcion porque no hay ningun curso que buscar
        return 
    #si encuntra al menos una coinsidencia se inicializa en false pone true cuando encuentra algo
    encontrado = False 

    #recorre la lista cursos
    #Si el usuario escribe ALGO encotrara ALGORITMOS
    for item in cursos: 
        #Imprime lo que encontro tal y como esta guardado 
        if nombre in item["curso"].lower():
            print(f"CURSO ENCONTRADO: {item['curso']}, NOTA: {item['nota']}")
            encontrado = True
    #si al terminar el bucle no se encuentra nada le avisamos al usuario
    if not encontrado:
        print("NO SE ENCONTRO NINGUN CURSO CON ESE NOMBRE LO SIENTO.")




#PROCEDIMIENTO ACTUALIZAR NOTA
# busca un curso por nombre y permite modificarle la nota
#valida que la nota nueva sea numerica y este dentro del rango establecido
def Actualizar_nota():
    nombre = input("INGRESE EL NOMBRE DEL CURSO A ACTUALIZAR:  ").strip()

    for item in cursos: 
        #si encuentra el curso pide que ingrese la nota nueva
        if item["curso"].lower() == nombre.lower():
            nueva = input("INGRESE LA NUEVA NOTA (0 A 100): ").strip()
            if nueva.isdigit():
                nueva = int(nueva)
                if 0 <= nueva <= 100:
                    item["nota"] = nueva
                    print("NOTA ACTUALIZADA CON EXITO")
                else: 
                    print("ERROR: LA NOTA DEBE DE ESTAR ENTRE 0 Y 100")
            else: 
                print("ERROR: LA NOTA DEBE DE SER UN DATO NUMERICO")
                #sale de la funcion despues de actualizar las notas
                return 
    #si no se encuentra el nombre en la lista 
    print("NO SE ENCOTRO NINGUN CURSO CON ESE NOMBRE")


#FUNCION ELIMINAR CUERSO
#ELIMINA un curso por nombre antes de borrarlo pide confirmacion
# si el usuario escribe SI lo elimina
# si el usuario escribe NO se cancela

def eliminar_curso():
    nombre = input("INGRESE EL NOMBRE DEL CURSO A ELIMINAR: ").strip()

    for i, item in enumerate(cursos): 
        if item["curso"].lower() == nombre.lower():
            confirmar = input(f"ESTA SUGURO DE QUE QUIERE ELIMINAR ESTE CURSO '{item['curso']}' (SI/NO): ").strip().lower()
            if confirmar == "si": 
                #se elimina el curso y la nota juntos
                eliminado = cursos.pop(i) 
                print(f"CURSO ELIMINADO CORRECTAMENTE")
            else: 
                print("ELIMINACION CANCELADA")
                return 
    print("NO SE ENCONTRO NINGUN CURSO CON ESE NOMBRE")

#####  ALGORITMOS DE ORDENAMIENTO #######

## FUNCION ORDENAMIENTO BURBUJA 
#Recorre toda la lista varias veces comparando pares de elemtos y los 
# va intercambiando en orden descendente va a ordenar las notas de mayor a menor 

def ordenamiento_de_notas_burbuja():
    #se repite n-1 veces
    n = len(cursos)
   #se repite n-1 veces
    for i in range(n-1): 
        #compara cada par en cada pasada
        for j in range(n-1-i): 
            #intercambia se esta en el orden incorrecto
            if  cursos[j]["nota"] < cursos [j+1]["nota"]: 
                cursos[j], cursos[j+1] = cursos[j+1], cursos[j]
    #muestra los resultados 
    print ("CURSOS ORDENADOS POR NOTA")
    for i, item in enumerate(cursos): 
        print(f"{i+1}. {item['curso']} - Nota: {item['nota']}")


#### FUNCION ORDENAMIENTO INSERCION 
#recorre la lista y va insertando cada elemento en la pocision que le corresponde
# va a ordenar por orden alfabetico segun el nombre ddel curso

def ordenamiento_de_curso_insercion(): 
    for i in range(1, len(cursos)): 
        clave = cursos[i]
        j = i - 1
        #mientras el nombre del curso sea menor al anterior se corre 
        while j >= 0 and clave ["curso"].lower() < cursos[j]["curso"].lower(): 
            cursos[j+1] = cursos[j]
            j -= 1
        cursos[j+1] = clave 
    #muestra resultados 
    print("CURSOS ORDENADOS POR NOMBRE")
    for i, item in enumerate(cursos): 
        print(f"{i+1}. {item['curso']} - Nota: {item['nota']}")


##### PILAS Y COLAS ######
#Funcion pila
#en historial=[] se van a guardar los cambios

def mostrar_historial(): 
    if not historial: 
        print("HISTORIAL VACIO")
    else: 
        print("HISTORIAL DE CAMBIOS")
        for i, evento in enumerate(reversed(historial), start=1): 
            print(f"{i}. {evento}")


#Funcion cola
# cola revicion de cursos 
#lista vacia se usa como cola
def cola_revision():
    cola_revision = []    

    print("INGRESE LOS CURSOS QUE DESEA REVISAR")
    print("ESCRIBA ´fin´ PARA TERMINAR.\n")

    while True: 
        nombre = input("CURSOS A REVISAR: ").strip()
        if nombre.lower() == "fin": 
            break
        if nombre == "": 
            print("ERROR: EL NOMBRE NO PUEDE ESTAR VACIO")
            continue 
        #se agrega al final de la cola 
        cola.append(nombre)
    
    #recorre la cola 
    print("\nPROCESANDO SOLICITUD DE REVISION")
    for curso in cola: 
        print(f"EL CURSO ´{curso}´ ESTA SIENDO REVISADO")
    
    print("TODAS LAS SOLICITUDES HAN SIDO ATENDIDAS")



      
###    MENU PRINCIPAL (MENU DE INICIO)
def menu(): 
    while True:
        print("=====GESTOR DE NOTAS ACADEMICAS 2025=====")
        print("1. REGISTRAR NUEVO CURSO")
        print("2. MOSTRAR TODOS LOS CURSOS Y NOTAS")  
        print("3. CALCULAR PROMEDIO GENERAL")
        print("4. CONTAR CURSOS APROBADOS Y REPROBADOS")
        #Aqui se hace la busqueda linal en buscar curso por nombre
        print("5. BUSCAR CURSOS POR NOMBRE")  
        print("6. ACTUALIZAR NOTA DE UN CURSO")
        print("7. ELIMINAR UN CURSO")
        print("8. ORDENAR CURSOS POR NOTA")
        print("9. ORDENAR CURSOS POR NOMBRE")
        print("10. MOSTRAR HISTORIAL")
        print("11. SOLICITAR REVISION")
        print("12. SALIR")
        opcion = input("SELECCIONE UNA OPCION DEL 1 AL 12: ").strip()

        if opcion == "1":
            registrar_cursos()
        elif opcion == "2":
            mostrar_curso()
        elif opcion == "3":
            promedio = Calcular_promedio()      
            if promedio is None: 
                print("NO SE PUEDE CALCULAR PROMEDIO PORQUE NO HAY CURSOS REGISTRADOS.")
            else:
                print(f"POMEDIO GENERAL: {promedio: .2f}")
        elif opcion == "4": 
            Contar_Aprobadas_y_Reprobadas()
        elif opcion == "5":
            Buscar_curso()
        elif opcion == "6":
            Actualizar_nota()
        elif opcion == "7":
            eliminar_curso()
        elif opcion == "8": 
            ordenamiento_de_notas_burbuja()
        elif opcion == "9":
            ordenamiento_de_curso_insercion()
        elif opcion == "10":
            mostrar_historial()
        elif opcion == "11":
            cola_revision()
        elif opcion == "12": 
            print("GRACIAS POR USAR EL GESTOR DE NOTAS")
            print("HASTA PRONTO")
            break
        else: 
            print("OPCION INVALIDA ENTENTE DE NUEVO CON OTRO NUMERO DEL 1 AL 12")



# AQUI INICIA EL PROGRAMA 
# LLAMAMOS AL MENU PRINCIPAL
menu()







           