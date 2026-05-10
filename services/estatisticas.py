# ESTATÍSTICAS
def mostrar_estatisticas(lista_produtos):

    if len(lista_produtos) == 0:

        print("\nNenhum produto registado.")

    else:

        # PRODUTO MAIS CARO
        produto_caro = lista_produtos[0]

        for produto in lista_produtos:

            if produto.preco > produto_caro.preco:

                produto_caro = produto

        print("\n=== PRODUTO MAIS CARO ===")

        produto_caro.mostrar()

        # MÉDIA DE PREÇOS
        soma_precos = 0

        for produto in lista_produtos:

            soma_precos += produto.preco

        media = soma_precos / len(lista_produtos)

        print(f"\nMédia de preços: {media:.2f} €")

        # TOTAL DE PRODUTOS
        total_produtos = len(lista_produtos)

        print(f"\nTotal de produtos: {total_produtos}")

        # VALOR TOTAL DO STOCK
        valor_stock = 0

        for produto in lista_produtos:

            valor_stock += produto.preco * produto.stock

        print(f"\nValor total do stock: {valor_stock:.2f} €")

        # ALERTAS DE STOCK
        print("\n=== ALERTAS DE STOCK ===")

        encontrou_alerta = False

        for produto in lista_produtos:

            # produtos caros
            if produto.preco >= 300:

                if produto.stock == 0:

                    print(
                        f"{produto.nome} -> QUEBRA DE STOCK!"
                    )

                    encontrou_alerta = True

                elif produto.stock <= 2:

                    print(
                        f"{produto.nome} -> ENCOMENDAR STOCK!"
                    )

                    encontrou_alerta = True

            # produtos normais
            else:

                if produto.stock == 0:

                    print(
                        f"{produto.nome} -> QUEBRA DE STOCK!"
                    )

                    encontrou_alerta = True

                elif produto.stock < 5:

                    print(
                        f"{produto.nome} -> STOCK BAIXO!"
                    )

                    encontrou_alerta = True

        if encontrou_alerta == False:

            print("Stock estável.")

        # PRODUTOS SEM STOCK
        print("\n=== PRODUTOS SEM STOCK ===")

        encontrou_sem_stock = False

        for produto in lista_produtos:

            if produto.stock == 0:

                produto.mostrar()

                encontrou_sem_stock = True

        if encontrou_sem_stock == False:

            print("Nenhum produto sem stock.")