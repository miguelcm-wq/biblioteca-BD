import sqlite3 

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS livros")

conn.execute("CREATE TABLE autores (id INTEGER PRIMARY KEY AUTOINCREMENT, \
             titulo TEXT NOT NULL, ano_publicacao INTEGER)")

conn.executemany("INSERT INTO autores(nome) VALUES(?)",
                 [("Desconhecido",), ("Cellbit",), ("Daniel",),])

conn.commit()