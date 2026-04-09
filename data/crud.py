import sqlite3

def crear(conn: sqlite3.Connection, nombre: str, correo: str, nota: float) -> None:
    conn.execute(
        "INSERT INTO estudiantes (nombre, correo, nota) VALUES (?, ?, ?)",
        (nombre, correo, nota)
    )
    conn.commit()

def leer(conn: sqlite3.Connection) -> list:
    cursor = conn.execute("SELECT * FROM estudiantes")
    return cursor.fetchall()

def actualizar(conn: sqlite3.Connection, id_estudiante: int, nueva_nota: float) -> None:
    conn.execute(
        "UPDATE estudiantes SET nota=? WHERE id=?",
        (nueva_nota, id_estudiante)
    )
    conn.commit()

def eliminar(conn: sqlite3.Connection, id_estudiante: int) -> None:
    conn.execute(
        "DELETE FROM estudiantes WHERE id=?",
        (id_estudiante,)
    )
    conn.commit()