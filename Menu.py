from Classes import Estudante, Livro, Emprestimo
import os 

opcao2 = 0
opcao = 0
while(opcao != 4):
    print("-----Menu de Opções-----")
    print("1 - Estudante")
    print("2 - Livro")
    print("3 - Emprestimo")
    opcao = int (input("digite a opção desejada: "))

    if(opcao == 1):
        print("-----Menu de Opções Estudante-----")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Excluir")
        opcao2 = int(input("digite a opção desejada"))


        if(opcao2 == 1):
            print("Cadastrando o Estudante...")
            nome_completo = input("Nome: ")
            idade = input("Idade: ")
            cpf = input("CPF: ")

            aluno = Estudante.create(nome=nome_completo, idade=idade, cpf=cpf)

            print (f"Estudante {aluno} cadsatrado com Sucesso")

            input("\n\nDigite ENTER para continuar...")
        

        if(opcao2 == 2):
            print("Estudantes Cadastrados")

            lista = Estudante.select()
            print("\nTotal de Estudantes:", len(lista), "\n")

            for est in lista:
                print(f"ID: {est.nome} - {est.idade} ({est.cpf})")

            input("\n\nDigite ENTER para continuar")
