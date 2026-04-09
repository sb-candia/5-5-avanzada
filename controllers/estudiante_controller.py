from data.crud import crear, leer, actualizar, eliminar
from models.estudiante import Estudiante

def crear_estudiante(conn, nombre, correo, nota):
    crear(conn, nombre, correo, nota)

def listar_estudiantes(conn):
    datos = leer(conn)
    estudiantes = []

    for d in datos:
        estudiante = Estudiante(d[0], d[1], d[2], d[3])
        estudiantes.append(estudiante)

    return estudiantes

def actualizar_estudiante(conn, id_estudiante, nueva_nota):
    actualizar(conn, id_estudiante, nueva_nota)

def eliminar_estudiante(conn, id_estudiante):
    eliminar(conn, id_estudiante)