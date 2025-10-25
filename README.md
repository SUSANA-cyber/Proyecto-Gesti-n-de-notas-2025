  Gestor de Notas Académicas 


Descripción 


El proyecto Gestor de Notas es un sistema que permite a los estudiantes llevar un control detallado de sus calificaciones de forma sencilla y organizada. Este sistema funcionará en consola y está diseñado para registrar, visualizar, modificar, eliminar, buscar y analizar las notas obtenidas en distintos cursos. 


Este programa está diseñado para estudiantes que necesitan una herramienta básica pero completa para tener un control eficiente de sus calificaciones, además incluye funcionalidades como el cálculo de promedios y  la identificación de cursos aprobados y reprobados. 


Además de ser útil en la práctica, este programa es una buena oportunidad para poner en práctica hábitos importantes al programar, como organizar el código en funciones claras, validar correctamente lo que ingrese el usuario y usar repeticiones de forma eficiente. Todo se desarrollara en consola 


Requisitos del sistema 
 
Funcionales 


* Registrar un nuevo curso y su nota 
* Mostrar todos los cursos registrados con su respectiva nota 
* Calcular el promedio general de todas las notas ingresadas 
* Contar cuántos cursos han sido aprobados y cuántos reprobados 
* Buscar un curso por su nombre 
* Actualizar las notas del curso
* Eliminar un curso registrado 


No funcionales 




* El lenguaje de programación para desarrollar el proyecto es Python 
* El programa se ejecuta en consola 
* No tiene interfaces gráficas 
* No requiere librerías externas 
* Debe de estar diseñadas con bucles y condicionales 
* Debe de estructurarse en Pseudocódigo para la planificación inicial 


Pseudocódigo



INICIO 


 Menú <- verdadero 


Mientras Menú Hacer 


IMPRIMIR “ Menu principal “
 
IMPRIMIR “1 agregar curso y nota”
 
IMPRIMIR “2 ver cursos guardados”
 
IMPRIMIR “3 calcular promedio”
  
IMPRIMIR “4 ver cuantos cursos estan aprobados y cuantos estan reprobados”
 
IMPRIMIR “5 buscar curso por nombre ”
 
IMPRIMIR “6 modificar nota de los cursos”
 
IMPRIMIR “7 salir”


LEER opciones 


SI opciones == 1 entonces 
<agregar curso>
SINO SI opciones == 2 entonces 
<ver cursos guardados>
SINO SI opciones == 3 entonces 
<calcular promedio>
SINO SI opciones == 4 entonces 
<mostrar cursos aprobados y reprobados>
SINO SI opciones == 5 entonces
<buscar curso>
SINO SI opciones == 6 entonces 
<modificar nota>
SINO SI opciones == 7 entonces 


IMPRIMIR “Salir”


opciones <- FALSO 
SINO 
IMPRIMIR “esa opcion no es valida ”


FIN SI 


FIN MIENTRAS 


FIN



                                          
                                                         ======REFLEXION=====
                                                                        
Aprendi que Python es un lenguaje de programación estructurado y muy flexible, que permite organizar las tareas de manera clara y mas sencilla usando funciones y proecedimientos. 

Este proyecto me ayudo a entender lo importante que es la modularización en Python. Al inicio yo queria resolver todo en una sola parte y se volvia un desorden, 
pero cuando empecé a separar cada tarea en funciones, todo se volvio mas claro y fácil de trabaja, me di cuenta de que dividir el código en partes pequeñas no 
solo ayuda a no confundirse, sino que tambien hace más sencillo encontrar y corregir errores, Ademas pude ver como las pilas, colas, busquedas y ordenamientos 
tienen sentido cuando se usan en algo real y no solo como ejercicios separados. Al final siento que este proyecto me ayudo a comprender mejor cómo pensar paso a paso 
y cómo organizar mis ideas antes de programar. 


¿Que aprendi con este proyecto?

Aprendi a modularizar mejor mi código usando funciones y a aplicar estructuras como listas, pilas y colas en un solo programa, tambien aprendi a validar entradas para evitar errores.
y apendi a escribir el código con una identación correcta, porque si no esta identado correctamente el código no funciona. Ademas comprendi lo util que es agregar comentarios al código
para explicar lo que cada parte hace y como funciona, esto ayuda a poder comprender mejor el programa y facilita las modificaciones futuras.

¿Que fue lo mas desafiante de resolver?

Lo mas deficil fue implementar el menú completo con todas las opciones y lograr que el programa no se cerrara cuando el usuario escribia algo incorrecto. Tambien me costo lograr que todos los algoritmos de busqueda
y ordenamiento funcionaran correctamente con la lista de curso y notas. de igual manera me resulto un poco dificil implementar el historial que registre todos los cambios, eliminación y actualización de manera correcta,
y validar que todas las entradas del usuario fueran validas y que el programa no se cerrara al ingresar algun dato mal.

¿Que mejoraria si tuviera más tiempo?

Mejoraria la precentacion del programa, creo que para el usuario seria mucho mas facil interacturar en el programa con interfaces graficas, tambien me gustaria poder separar las funciones en distintos archivos.
Podria implementar que se guarde la información en archivos para que al cerrar el programa no se pierda la información, y tambien poder agregar mas funciones relaciondas con reportes y tareas. 










