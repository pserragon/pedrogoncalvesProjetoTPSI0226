
# EXPORTAÇÃO DE DADOS BYTE TECH

# exportação de dados

def menu_exportacao(lista_produtos):

    try:

        password = input(
            "\nIntroduza a password: "
        )


        # validar password

        if password != "ByteTech123":

            print("\nAcesso negado.")
            return


        print("\nAcesso autorizado.")


        # menu exportação

        print("\n===== EXPORTAÇÃO =====")
        print("1 - Exportar produtos")
        print("2 - Exportar alertas")
        print("0 - Voltar")


        opcao = input("\nEscolha uma opção: ")


        # exportar produtos

        if opcao == "1":

            with open(

                "produtos_exportados.txt",
                "w",
                encoding="utf-8"

            ) as ficheiro:


                ficheiro.write(
                    "===== PRODUTOS BYTE TECH =====\n"
                )


                for produto in lista_produtos:

                    ficheiro.write(

                        f"""

ID: {produto.id}
Nome: {produto.nome}
Preço: {produto.preco} €
Stock: {produto.stock}
Categoria: {produto.categoria}
Empresa: {produto.empresa}

----------------------------

"""

                    )


            print(

                "\nProdutos exportados com sucesso!"

            )


        # exportar alertas

        elif opcao == "2":

            with open(

                "alertas_stock.txt",
                "w",
                encoding="utf-8"

            ) as ficheiro:


                ficheiro.write(
                    "===== ALERTAS STOCK =====\n"
                )


                for produto in lista_produtos:


                    # produtos caros

                    if produto.preco >= 300:

                        if produto.stock == 0:

                            ficheiro.write(

                                f"{produto.nome}"
                                f" -> QUEBRA DE STOCK\n"

                            )

                        elif produto.stock <= 2:

                            ficheiro.write(

                                f"{produto.nome}"
                                f" -> ENCOMENDAR STOCK\n"

                            )


                    # produtos normais

                    else:

                        if produto.stock == 0:

                            ficheiro.write(

                                f"{produto.nome}"
                                f" -> QUEBRA DE STOCK\n"

                            )

                        elif produto.stock < 5:

                            ficheiro.write(

                                f"{produto.nome}"
                                f" -> STOCK BAIXO\n"

                            )


            print(

                "\nAlertas exportados com sucesso!"

            )


        # voltar

        elif opcao == "0":

            return


        else:

            print("\nOpção inválida.")


    except Exception as erro:

        print(f"\nErro na exportação: {erro}")