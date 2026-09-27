import sqlite3 as sqlite

def listar_autores():
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autores")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"id: {linha['id']} | nome: {linha['nome']}")

    conn.close()