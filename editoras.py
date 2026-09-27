import sqlite3 as sqlite

def listar_editoras():
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM editoras")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"id: {linha['id']} | nome: {linha['nome']}")

    conn.close()