import sqlite3 

conn = sqlite3.connect("biblioteca.db")

conn.execute("DROP TABLE IF EXISTS editoras")

tabela_livros = """CREATE TABLE"""