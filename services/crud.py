# CRUD BYTE TECH

import re

from models.produto import Produto


# adicionar produto

def adicionar_produto(lista_produtos):

    try:

        # gerar id automático

        if len(lista_produtos) == 0:

            id = 1

        else:

            id = lista_produtos[-1].id + 1

        print(f"\nID gerado automaticamente: {id}")

        nome = input("Nome: ")

        preco = float(input("Preço: "))

        stock = int(input("Stock: "))

        categoria = input("Categoria: ")


        # validar empresa

        empresa = input("Empresa: ")

        padrao_empresa = r"^[A-Za-zÀ-ÿ\s]+$"

        resultado_empresa = re.match(
            padrao_empresa,
            empresa
        )

        if resultado_empresa is None:

            print("\nEmpresa inválida.")
            return

        else:

            print(
                "Regex empresa:",
                resultado_empresa.group()
            )

            print(
                "Posição:",
                resultado_empresa.span()
            )


        # validar email

        email = input("Email: ")

        padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        resultado_email = re.match(
            padrao_email,
            email
        )

        if resultado_email is None:

            print("\nEmail inválido.")
            return

        else:

            print(
                "Regex email:",
                resultado_email.group()
            )

            print(
                "Posição:",
                resultado_email.span()
            )


        # validar telefone

        telefone = input("Telefone: ")

        padrao_telefone = r"^9[1236][0-9]{7}$"

        resultado_telefone = re.match(
            padrao_telefone,
            telefone
        )

        if resultado_telefone is None:

            print("\nTelefone inválido.")
            return

        else:

            print(
                "Regex telefone:",
                resultado_telefone.group()
            )

            print(
                "Posição:",
                resultado_telefone.span()
            )


        # criar produto

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

        print("\nValores inválidos.")

    except Exception as erro:

        print(f"\nErro ao adicionar produto: {erro}")


# listar produtos

def listar_produtos(lista_produtos):

    try:

        if len(lista_produtos) == 0:

            print("\nNenhum produto registado.")

        else:

            print("\n===== LISTA DE PRODUTOS =====")

            for produto in lista_produtos:

                produto.mostrar()

    except Exception as erro:

        print(f"\nErro ao listar produtos: {erro}")


# editar produto

def editar_produto(lista_produtos):

    try:

        id_editar = int(
            input("\nID do produto a editar: ")
        )

        encontrado = False

        for produto in lista_produtos:

            if produto.id == id_editar:

                encontrado = True

                while True:

                    print("\n===== EDITAR PRODUTO =====")
                    print("1 - Nome")
                    print("2 - Preço")
                    print("3 - Stock")
                    print("4 - Categoria")
                    print("5 - Empresa")
                    print("6 - Email")
                    print("7 - Telefone")
                    print("0 - Voltar")

                    opcao_editar = input(
                        "\nEscolha uma opção: "
                    )


                    # editar nome

                    if opcao_editar == "1":

                        produto.nome = input(
                            "Novo nome: "
                        )

                        print("\nNome atualizado.")


                    # editar preço

                    elif opcao_editar == "2":

                        produto.preco = float(
                            input("Novo preço: ")
                        )

                        print("\nPreço atualizado.")


                    # editar stock

                    elif opcao_editar == "3":

                        produto.stock = int(
                            input("Novo stock: ")
                        )

                        print("\nStock atualizado.")


                    # editar categoria

                    elif opcao_editar == "4":

                        produto.categoria = input(
                            "Nova categoria: "
                        )

                        print("\nCategoria atualizada.")


                    # editar empresa

                    elif opcao_editar == "5":

                        nova_empresa = input(
                            "Nova empresa: "
                        )

                        padrao_empresa = r"^[A-Za-zÀ-ÿ\s]+$"

                        resultado_empresa = re.match(
                            padrao_empresa,
                            nova_empresa
                        )

                        if resultado_empresa:

                            produto.empresa = nova_empresa

                            print(
                                "\nEmpresa atualizada."
                            )

                        else:

                            print(
                                "\nEmpresa inválida."
                            )


                    # editar email

                    elif opcao_editar == "6":

                        novo_email = input(
                            "Novo email: "
                        )

                        padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

                        resultado_email = re.match(
                            padrao_email,
                            novo_email
                        )

                        if resultado_email:

                            produto.email = novo_email

                            print(
                                "\nEmail atualizado."
                            )

                        else:

                            print(
                                "\nEmail inválido."
                            )


                    # editar telefone

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
                                "\nTelefone atualizado."
                            )

                        else:

                            print(
                                "\nTelefone inválido."
                            )


                    # voltar

                    elif opcao_editar == "0":

                        break


                    # opção inválida

                    else:

                        print("\nOpção inválida.")

                break


        if encontrado is False:

            print("\nProduto não encontrado.")

    except ValueError:

        print("\nValores inválidos.")

    except Exception as erro:

        print(f"\nErro ao editar produto: {erro}")


# eliminar produto

def eliminar_produto(lista_produtos):

    try:

        id_eliminar = int(
            input("\nID do produto a eliminar: ")
        )

        encontrado = False

        for produto in lista_produtos:

            if produto.id == id_eliminar:

                encontrado = True

                confirmacao = input(

                    f"\nTem a certeza que deseja eliminar {produto.nome}? (s/n): "

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

                break


        if encontrado is False:

            print("\nProduto não encontrado.")

    except ValueError:

        print("\nValores inválidos.")

    except Exception as erro:

        print(f"\nErro ao eliminar produto: {erro}")