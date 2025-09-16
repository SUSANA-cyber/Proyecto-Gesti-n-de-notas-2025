# #funciones 
# #Muestra la lista completa de las paginas que estan en la pila 
# def mostrar_historial(paginas):
#     print("HISTORIAL", paginas)
    
# #simula visitar una nueva pagina 
# #agregamos la pagina al final de la lista con append()
# #mostramoa la pagina visitada y el historial actualizado

# def visitar_pagina(paginas, pagina):
#     paginas.append(pagina)
#     print("PAGINA VISITADA:", pagina)
#     mostrar_historial(paginas)

# #simula el boton de atras del boton del navegador
# #si la lista esta vacia no se puede retroceder 
# #si tienepaginas quitamos la ultima con pop()
# #mostramos cual se quito y el historial 

# def atras(paginas):

#     if not paginas:
#         print("NO HAY PAGINAS EN EL HISTORIAL")
#     else: 
#         quitada = paginas.pop()
#         print("SE QUITO", quitada)
#         mostrar_historial(paginas)


# # salir del programa 
# # Atras retrocede la retrosede la pagina 
# # devuelve false si se debe terminar true si el programa sigue

# def procesar_entrada(paginas, entrada):
    
#     entrada_normalizada = entrada.strip()
#     comando = entrada_normalizada.upper()
    
#     if comando == "SALIR":
#         print("FIN DEL PROGRAMA")
#         return False
#     elif comando == "ATRAS" or comando == "ATRAS":
#         atras(paginas)
#         return True
#     else:
#         visitar_pagina(paginas, entrada_normalizada)
#         return True
    
    
# #Progrma principal
# #pila vacia de navegacion (vacia)

# paginas = []

# print("SIMULADOR DE HISTORIAL")
# print("ESCRIBE UNA PAGINA WEB, ´ATRAS´ PARA RETROSEDER O ´SALIR´ PARA TERMINAR.\n  ")


# while True:
#     entrada = input("INGRESE UNA PAGINA WEB O ESCRIBA ´ATRAS´ O ´SALIR´:\n> ").strip()
    
#     #si el usuario no ingresa nada se le vuelve a pedir que intente de nuevo
#     if entrada == "":
#         print("NO SE A INGRESADO NADA. INTENTE DE NUEVO.\n ")
#         continue 
    
#     continuar = procesar_entrada(paginas, entrada)
    
#     #mostramos una linea separadora para que la salida sea clara
#     print("_" * 40)
    
    
#     #cuando el usuario escriba salir termina el bucle
    
#     if not continuar:
#         break
              
              

    
    
#"busqueda lineal y vinaria clase 09"

def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista [i] == valor:
            return i 
        return -1

lista = [4,7,8,9,3,4,6,10]
print(busqueda_lineal (lista, 10))
    
    