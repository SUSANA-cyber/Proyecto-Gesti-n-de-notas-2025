# Simulación de atención de pacientes en una clínica usando una cola (FIFO)

# Creamos una lista vacía para la cola
cola = []

# Registrar 5 pacientes
for i in range(1, 6):
    nombre = input(f"Ingrese el nombre del paciente {i}: ")
    cola.append(nombre)

# Mostrar la cola inicial
print("\nCola inicial de pacientes:")
print(cola)
print()

# Atender pacientes en orden
while len(cola) > 0:
    paciente = cola.pop(0)  # eliminar el primero (índice 0)
    print(f"Atendiendo a: {paciente}")
    print("Cola actualizada:", cola)
    print()

# Mensaje final
print("No quedan pacientes en la cola.")
