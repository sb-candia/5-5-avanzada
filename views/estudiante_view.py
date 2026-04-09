def menu():
    print("\n--- SISTEMA DE ESTUDIANTES ---")
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Actualizar nota")
    print("4. Eliminar estudiante")
    print("5. Salir")

def pedir_datos_crear():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    nota = float(input("Nota: "))
    return nombre, correo, nota

def pedir_id():
    return int(input("ID: "))

def pedir_nueva_nota():
    return float(input("Nueva nota: "))

def mostrar_estudiantes(estudiantes):
    for e in estudiantes:
        print(e)