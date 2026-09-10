import sqlite3 

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS editoras")

sql_create = """CREATE TABLE livros (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT NOT NULL, autor_id INTEGER REFERENCES autores(id), 
            editora_id INTEGER REFERENCES editoras(id),
            ano_publicacao INTEGER,
            edicao INTEGER,
            disponivel BOOLEAN NOT NULL DEFAULT 1 CHECK (disponivel IN(0,1)))"""

conn.execute(sql_create)

sql_insert = """INSERT INTO livros(titulo, autor_id, editora_id, ano_publicacao, edicao,
    disponivel) VALUES(?, ?, ?, ?, ?, ?)"""
 
conn.executemany(sql_insert, 
    [("Java como programar", 1, 2, 2000, 2, 1), 
     ("Python para iniciantes", 2, 1, 2020, 1, 0)])

conn.commit()