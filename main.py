from database.conexion import conectar, crear_tabla
from controllers.estudiante_controller import (
    crear_estudiante,
    listar_estudiantes,
    actualizar_estudiante,
    eliminar_estudiante
)
from views.estudiante_view import (
    menu,
    pedir_datos_crear,
    pedir_id,
    pedir_nueva_nota,
    mostrar_estudiantes
)

def main():
    conn = conectar()
    crear_tabla(conn)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre, correo, nota = pedir_datos_crear()
            crear_estudiante(conn, nombre, correo, nota)

        elif opcion == "2":
            estudiantes = listar_estudiantes(conn)
            mostrar_estudiantes(estudiantes)

        elif opcion == "3":
            id_estudiante = pedir_id()
            nueva_nota = pedir_nueva_nota()
            actualizar_estudiante(conn, id_estudiante, nueva_nota)

        elif opcion == "4":
            id_estudiante = pedir_id()
            eliminar_estudiante(conn, id_estudiante)

        elif opcion == "5":
            break

        else:
            print("Opción no válida.")

    conn.close()

if __name__ == "__main__":
    main()