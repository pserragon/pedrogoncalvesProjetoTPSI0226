import re

from models.produto import Produto


# ADICIONAR PRODUTO
def adicionar_produto(lista_produtos):

    try:

        # gerar ID automático
        if len(lista_produtos) == 0:

            id = 1

        else:

            id = lista_produtos[-1].id + 1

        print(f"\nID gerado automaticamente: {id}")

        nome = input("Nome: ")
        preco = float(input("Preço: "))
        stock = int(input("Stock: "))
        categoria = input("Categoria: ")

        # REGEX EMPRESA
        empresa = input("Empresa: ")

        padrao_empresa = r"^[A-Za-zÀ-ÿ\s]+$"

        resultado_empresa = re.match(
            padrao_empresa,
            empresa
        )

        if resultado_empresa:

            print("\nEmpresa válida!")
            print("Match:", resultado_empresa.group())
            print("Posição:", resultado_empresa.span())

        else:

            print("\nEmpresa inválida!")
            return

        # REGEX EMAIL
        email = input("Email: ")

        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        resultado = re.match(padrao, email)

        if resultado:

            print("\nEmail válido!")
            print("Match:", resultado.group())
            print("Posição:", resultado.span())

        else:

            print("\nEmail inválido!")
            return

        # REGEX TELEFONE
        telefone = input("Telefone: ")

        padrao_telefone = r"^9[1236][0-9]{7}$"

        resultado_telefone = re.match(
            padrao_telefone,
            telefone
        )

        if resultado_telefone:

            print("\nTelefone válido!")
            print("Match:", resultado_telefone.group())
            print("Posição:", resultado_telefone.span())

        else:

            print("\nTelefone inválido!")
            return

        produto = Produto(
            id,
            nome,
            preco,
            stock,
            categoria,
            empresa,
            email,
            telefone
        )

        lista_produtos.append(produto)

        print("\nProduto adicionado com sucesso!")

    except ValueError:

        print("\nERRO: Introduziu valores inválidos.")


# LISTAR PRODUTOS
def listar_produtos(lista_produtos):

    if len(lista_produtos) == 0:

        print("\nNenhum produto registado.")

    else:

        print("\n=== LISTA DE PRODUTOS ===")

        for produto in lista_produtos:

            produto.mostrar()


# EDITAR PRODUTO
def editar_produto(lista_produtos):

    try:

        id_editar = int(input("ID do produto a editar: "))

        encontrado = False

        for produto in lista_produtos:

            if produto.id == id_editar:

                encontrado = True

                while True:

                    print("\n=== EDITAR PRODUTO ===")
                    print("1 - Nome")
                    print("2 - Preço")
                    print("3 - Stock")
                    print("4 - Categoria")
                    print("5 - Empresa")
                    print("6 - Email")
                    print("7 - Telefone")
                    print("0 - Voltar")

                    opcao_editar = input(
                        "Escolha uma opção: "
                    )

                    if opcao_editar == "1":

                        produto.nome = input(
                            "Novo nome: "
                        )

                        print(
                            "\nNome atualizado com sucesso!"
                        )

                    elif opcao_editar == "2":

                        produto.preco = float(
                            input("Novo preço: ")
                        )

                        print(
                            "\nPreço atualizado com sucesso!"
                        )

                    elif opcao_editar == "3":

                        produto.stock = int(
                            input("Novo stock: ")
                        )

                        print(
                            "\nStock atualizado com sucesso!"
                        )

                    elif opcao_editar == "4":

                        produto.categoria = input(
                            "Nova categoria: "
                        )

                        print(
                            "\nCategoria atualizada com sucesso!"
                        )

                    elif opcao_editar == "5":

                        produto.empresa = input(
                            "Nova empresa: "
                        )

                        print(
                            "\nEmpresa atualizada com sucesso!"
                        )

                    elif opcao_editar == "6":

                        novo_email = input(
                            "Novo email: "
                        )

                        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

                        resultado = re.match(
                            padrao,
                            novo_email
                        )

                        if resultado:

                            produto.email = novo_email

                            print(
                                "\nEmail atualizado com sucesso!"
                            )

                            print(
                                "Match:",
                                resultado.group()
                            )

                            print(
                                "Posição:",
                                resultado.span()
                            )

                        else:

                            print(
                                "\nEmail inválido!"
                            )

                    elif opcao_editar == "7":

                        novo_telefone = input(
                            "Novo telefone: "
                        )

                        padrao_telefone = r"^9[1236][0-9]{7}$"

                        resultado_telefone = re.match(
                            padrao_telefone,
                            novo_telefone
                        )

                        if resultado_telefone:

                            produto.telefone = novo_telefone

                            print(
                                "\nTelefone atualizado com sucesso!"
                            )

                        else:

                            print(
                                "\nTelefone inválido!"
                            )

                    elif opcao_editar == "0":

                        break

                    else:

                        print("\nOpção inválida.")

        if encontrado == False:

            print("\nProduto não encontrado.")

    except ValueError:

        print("\nERRO: Introduziu valores inválidos.")


# ELIMINAR PRODUTO
def eliminar_produto(lista_produtos):

    try:

        id_eliminar = int(
            input("ID do produto a eliminar: ")
        )

        encontrado = False

        for produto in lista_produtos:

            if produto.id == id_eliminar:

                confirmacao = input(
                    f"Tem a certeza que deseja eliminar {produto.nome}? (s/n): "
                ).lower()

                if confirmacao == "s":

                    lista_produtos.remove(produto)

                    print(
                        "\nProduto eliminado com sucesso!"
                    )

                else:

                    print(
                        "\nEliminação cancelada."
                    )

                encontrado = True
                break

        if encontrado == False:

            print("\nProduto não encontrado.")

    except ValueError:

        print("\nERRO: Introduziu valores inválidos.")