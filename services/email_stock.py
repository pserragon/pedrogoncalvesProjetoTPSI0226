
# EMAIL STOCK BYTE TECH

# gerar email stock baixo

def gerar_email_stock(lista_produtos):

    try:

        produtos_alerta = []


        # procurar produtos com alerta

        for produto in lista_produtos:

            # produtos caros

            if produto.preco >= 300:

                if produto.stock <= 2:

                    produtos_alerta.append(produto)


            # produtos normais

            else:

                if produto.stock < 5:

                    produtos_alerta.append(produto)


        # sem produtos

        if len(produtos_alerta) == 0:

            print("\nNenhum produto com stock baixo.")
            return


        # mostrar produtos

        print("\n===== PRODUTOS COM ALERTA =====")

        for i, produto in enumerate(produtos_alerta):

            print(

                f"{i + 1} - {produto.nome} "
                f"(Stock: {produto.stock})"

            )


        # escolher produto

        escolha = int(

            input("\nEscolha um produto: ")

        ) - 1


        # validar escolha

        if escolha < 0 or escolha >= len(produtos_alerta):

            print("\nOpção inválida.")
            return


        produto = produtos_alerta[escolha]


        # escrever mensagem

        mensagem = input(

            "\nMensagem para o fornecedor: "

        )


        # mostrar email

        print("\n===== EMAIL GERADO =====")

        print(f"\nPARA: {produto.email}")

        print(

            f"\nASSUNTO: Reposição de Stock - "
            f"{produto.nome}"

        )

        print("\nMENSAGEM:")

        print(f"""

Boa tarde {produto.empresa},

Solicitamos reposição de stock do produto:

{produto.nome}

Stock atual:
{produto.stock} unidades

Mensagem adicional:
{mensagem}

Cumprimentos,
ByteTech

""")

        input("\nPressione ENTER para voltar ao menu...")

    except ValueError:

        print("\nValor inválido.")

    except Exception as erro:

        print(f"\nErro ao gerar email: {erro}")