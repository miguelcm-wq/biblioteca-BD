from usuarios import listar_usuarios, cadastrar_usuario
from autores import listar_autores
from editoras import listar_editoras
from livros import cadastrar_livros

while(True):
    print('\n1 - Usuário')
    print('2 - Autores')
    print('3 - Editores')
    print('4 - Livros')
    print('5 - Emprestimos')
    print('6 - Histórico')
    menu = int(input(('Digite: ')))

    if (menu == 1):
        while(True):
            print('\n1 - Cadastrar usuário')
            print('2 - Listar usuários')
            print('3 - Voltar')
            menu_usuario = int(input('Digite: '))

            if (menu_usuario == 1):
                cadastrar_usuario()
                break

            elif (menu_usuario == 2):
                print('\n=== LISTA DE USUÁRIOS ===\n')
                listar_usuarios()
                break

            elif (menu_usuario == 3):
                break

            else:
                print('\nAlgo deu errado!\nTente novamente.')

    elif (menu == 2):
        print('\n=== LISTA DE AUTORES ===\n')
        listar_autores()

    elif (menu == 3):
        print('\n=== LISTA DE EDITORAS ===\n')
        listar_editoras()

    elif (menu == 4):
        while(True):
            print('\n1 - Cadastrar livro')
            print('2 - Listar livros')
            print('3 - Voltar')
            menu_livro = int(input('Digite: '))

            if (menu_livro == 1):
                cadastrar_livros()
                break

            elif (menu_livro == 2):
                pass
                break

            elif (menu_livro == 3):
                break

            else:
                print('\nAlgo deu errado!\nTente novamente.')

    elif (menu == 5):
        while(True):
            print('\n1 - Fazer emprestimo')
            print('2 - Listar emprestimos')
            print('3 - Voltar')
            menu_emprestimo = int(input('Digite: '))

            if (menu_emprestimo == 1):
                pass
                break

            elif (menu_emprestimo == 2):
                pass
                break

            elif (menu_emprestimo == 3):
                break

            else:
                print('\nAlgo deu errado!\nTente novamente.')

    elif (menu == 6):
        pass
        
    else:
        print('\nAlgo deu errado!\nTente novamente.')