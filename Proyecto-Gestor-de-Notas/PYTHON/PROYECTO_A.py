
#print("hola mundo")
#input
#"""



#3
# N = 23
#A = 25
#suma = A + N
#print ("total suma", suma)

#s = int (input ("numero"))
#l = int (input ("numero"))
#suma = s+l
#print ("total suma", suma

#def mostrar 

#numero = int(input("ingrese un numero: "))
#for i  in range (0, numero + 1 ):
#print ("hola")

# imprime hola n veces

#numero = int(input("ingrese su numero: "))
#for i in range (numero):
   # print("hola")

   #CLASE 30-08.2025
   #TEMA LISTAS


   #LISTA_ENTERO = [1,2,3,4]

   #LISTA_ENTERO [-2]

#LISTA_NOMBRES

#UNION DE LISTAS, LISTAS_NOMBRE + NOMBRE
 
#NUEVA_LISTAS ["MUGUEL, SUSANA, ALDO"]
#NUMEROS [1,2,3,4]
#NUEVO = NUEVA_LISTA + NUMEROS
#slice_1 


#def operacion_lista(lista):
# lista_1 = lista
# lista_1.append("josue")


#lis<<ta_original 

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
            indice = int(indice)
            if 0 <= indice < len(Notas):
                nueva = input("ingrese la nota 0 a 100")
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


                  

            
        
    









