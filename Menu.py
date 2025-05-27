from Classes import Estudante, Livro, Emprestimo
import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    limpar()
    print("-----Menu de Opções-----")
    print("1 - Estudante")
    print("2 - Livro")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        limpar()
        print("-----Menu Estudante-----")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        opcao2 = int(input("Digite a opção desejada: "))

        if opcao2 == 1:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cpf = input("CPF: ")
            Estudante.create(nome=nome, idade=idade, cpf=cpf)
            print("Estudante cadastrado com sucesso.")
            input("\nDigite ENTER para continuar...")

        elif opcao2 == 2:
            print("Estudantes Cadastrados:")
            for est in Estudante.select():
                print(est)
            input("\nDigite ENTER para continuar...")

        elif opcao2 == 3:
            cpf = input("CPF do estudante a editar: ")
            try:
                est = Estudante.get(Estudante.cpf == cpf)
                est.nome = input(f"Novo nome ({est.nome}): ") or est.nome
                est.idade = int(
                    input(f"Nova idade ({est.idade}): ") or est.idade)
                est.save()
                print("Estudante atualizado com sucesso.")
            except Estudante.DoesNotExist:
                print("Estudante não encontrado.")
            input("\nDigite ENTER para continuar...")

        elif opcao2 == 4:
            cpf = input("CPF do estudante a excluir: ")
            try:
                est = Estudante.get(Estudante.cpf == cpf)
                est.delete_instance()
                print("Estudante excluído com sucesso.")
            except Estudante.DoesNotExist:
                print("Estudante não encontrado.")
            input("\nDigite ENTER para continuar...")

    elif opcao == 2:
        limpar()
        print("-----Menu Livro-----")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        opcao2 = int(input("Digite a opção desejada: "))

        if opcao2 == 1:
            nome = input("Nome do livro: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            Livro.create(nome=nome, autor=autor, categoria=categoria)
            print("Livro cadastrado com sucesso.")
            input("\nDigite ENTER para continuar...")

        elif opcao2 == 2:
            print("Livros Cadastrados:")
            for livro in Livro.select():
                print(livro)
            input("\nDigite ENTER para continuar...")

        elif opcao2 == 3:
            id_livro = input("ID do livro a editar: ")
            try:
                livro = Livro.get_by_id(id_livro)
                livro.nome = input(f"Novo nome ({livro.nome}): ") or livro.nome
                livro.autor = input(
                    f"Novo autor ({livro.autor}): ") or livro.autor
                livro.categoria = input(
                    f"Nova categoria ({livro.categoria}): ") or livro.categoria
                livro.save()
                print("Livro atualizado com sucesso.")
            except Livro.DoesNotExist:
                print("Livro não encontrado.")
            input("\nDigite ENTER para continuar...")

        elif opcao2 == 4:
            id_livro = input("ID do livro a excluir: ")
            try:
                livro = Livro.get_by_id(id_livro)
                livro.delete_instance()
                print("Livro excluído com sucesso.")
            except Livro.DoesNotExist:
                print("Livro não encontrado.")
            input("\nDigite ENTER para continuar...")

    elif opcao == 3:
        print("Sistema encerrado.")
        break
