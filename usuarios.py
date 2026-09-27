import sqlite3 as sqlite

def cadastrar_usuario():
    conn = sqlite.connect("biblioteca.db")
   
    nome = input('\nDigite o nome do usuário: ')

    conn.execute("INSERT INTO usuarios(nome) VALUES(?)", (nome,))

    print('\nUsuário adicionado com sucesso!')
   
    conn.commit()
   
def listar_usuarios():
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")

    resultados = cursor.fetchall()

    for linha in resultados:
        print(f"id: {linha['id']} | nome: {linha['nome']}")

    conn.close()