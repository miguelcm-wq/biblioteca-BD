import sqlite3 as sqlite

def cadastrar_livros():
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row
    cursor = conn.cursor()
    ja_tem_autor = False
    ja_tem_editora = False

    sql_insert = """INSERT INTO livros(titulo, autor_id, editora_id, ano_publicacao, edicao,
    disponivel) VALUES(?, ?, ?, ?, ?, ?)"""

    titulo = input('\nDigite o título do livro: ')

    autor = input('Digite o nome do autor: ')

    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()
    for verificar_autor in autores:
        if verificar_autor['nome'] == autor:
            ja_tem_autor == True
        else:
            pass
    if ja_tem_autor == True:
        pass
    else:
        conn.execute("INSERT INTO autores(nome) VALUES(?)", (autor,))
        conn.commit()

    editora = input('Digite o nome da editora: ')
    

    cursor.execute("SELECT * FROM editoras")
    editoras = cursor.fetchall() 
    for verificar_editora in editoras:
        if (verificar_editora['nome'] == editora):
            ja_tem_editora == True
        else:
            pass
        if (ja_tem_editora == True):
            pass
        else:
            conn.execute("INSERT INTO editoras(nome) VALUES(?)", (editora,))
            conn.commit()

    ano_publicacao = int(input('Digite o ano de publicação do livro: '))

    edicao = int(input('Digite a edição do livro: '))
    while(True):
        disponivel = ('Digite 1 para disponível e 2 para indisponível: ')
        if (disponivel == 1):
            disponivel == True
            break
        elif (disponivel == 2):
            disponivel == False
            break
        else:
            print('\nAlgo deu errado!\nTente novamente.')

        comando_sql1 = ("SELECT id FROM autores WHERE nome = ?")
        cursor.execute(comando_sql1, (autor,))
        id_autor = cursor.fetchone()
        
        comando_sql2 = ("SELECT id FROM editoras WHERE nome = ?")
        cursor.execute(comando_sql2, (editora,))
        id_editora = cursor.fetchone()

    conn.execute(sql_insert, (titulo, id_autor, id_editora, ano_publicacao, edicao, disponivel))
   
    conn.commit()

def listar_livros():
    conn = sqlite.connect("biblioteca.db")
    conn.row_factory = sqlite.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")

    resultados = cursor.fetchall()

    for linha in resultados:
        if(linha('disponivel' == True)):
            print(f"id: {linha['id']} | título: {linha['titulo']} | autor: {linha['']} | editora: {linha['']} | ano publicação: {linha['']} | edição: {linha['']} | está disponível")
        elif(linha('disponivel' == True)):
            print(f"id: {linha['id']} | título: {linha['titulo']} | autor: {linha['']} | editora: {linha['']} | ano publicação: {linha['']} | edição: {linha['']} | está indisponível")

    conn.close()