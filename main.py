import sqlite3

def buscar_usuario_seguro(username):
    # ✅ SEGURO: uso de parâmetros preparados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = "SELECT * FROM usuarios WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()