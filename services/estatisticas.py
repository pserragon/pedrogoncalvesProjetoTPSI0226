
# ESTATÍSTICAS BYTE TECH

# estatísticas

def mostrar_estatisticas(lista_produtos):

    try:

        if len(lista_produtos) == 0:

            print("\nNenhum produto registado.")
            return


        # produto mais caro

        produto_caro = lista_produtos[0]

        for produto in lista_produtos:

            if produto.preco > produto_caro.preco:

                produto_caro = produto


        print("\n===== PRODUTO MAIS CARO =====")

        produto_caro.mostrar()

        print(f"\nPreço: {produto_caro.preco:.2f} €")


        # média preços

        soma_precos = 0

        for produto in lista_produtos:

            soma_precos += produto.preco

        media = soma_precos / len(lista_produtos)

        print(f"\nMédia de preços: {media:.2f} €")


        # total produtos

        total_produtos = len(lista_produtos)

        print(f"\nTotal de produtos: {total_produtos}")


        # valor total stock

        valor_stock = 0

        for produto in lista_produtos:

            valor_stock += produto.preco * produto.stock

        print(

            f"\nValor total do stock: {valor_stock:.2f} €"

        )


        # alertas stock

        print("\n===== ALERTAS DE STOCK =====")

        encontrou_alerta = False


        for produto in lista_produtos:


            # produtos caros

            if produto.preco >= 300:

                if produto.stock == 0:

                    print(

                        f"{produto.nome} -> QUEBRA DE STOCK"

                    )

                    encontrou_alerta = True


                elif produto.stock <= 2:

                    print(

                        f"{produto.nome} -> ENCOMENDAR STOCK"

                    )

                    encontrou_alerta = True


            # produtos normais

            else:

                if produto.stock == 0:

                    print(

                        f"{produto.nome} -> QUEBRA DE STOCK"

                    )

                    encontrou_alerta = True


                elif produto.stock < 5:

                    print(

                        f"{produto.nome} -> STOCK BAIXO"

                    )

                    encontrou_alerta = True


        if encontrou_alerta is False:

            print("\nStock estável.")


        # produtos sem stock

        print("\n===== PRODUTOS SEM STOCK =====")

        encontrou_sem_stock = False


        for produto in lista_produtos:

            if produto.stock == 0:

                produto.mostrar()

                encontrou_sem_stock = True


        if encontrou_sem_stock is False:

            print("\nNenhum produto sem stock.")

    except Exception as erro:

        print(f"\nErro ao mostrar estatísticas: {erro}")


# filtro preço acima

def filtrar_preco_acima(lista_produtos, valor):

    try:

        encontrados = []

        for produto in lista_produtos:

            if produto.preco > valor:

                encontrados.append(produto)

        return encontrados

    except Exception as erro:

        print(f"\nErro no filtro de preço: {erro}")

        return []


# filtro intervalo preço

def filtrar_intervalo_preco(

    lista_produtos,
    minimo,
    maximo

):

    try:

        encontrados = []

        for produto in lista_produtos:

            if minimo <= produto.preco <= maximo:

                encontrados.append(produto)

        return encontrados

    except Exception as erro:

        print(f"\nErro no filtro de intervalo: {erro}")

        return []


# filtro stock baixo

def filtrar_stock_baixo(lista_produtos):

    try:

        encontrados = []

        for produto in lista_produtos:

            if produto.stock < 5:

                encontrados.append(produto)

        return encontrados

    except Exception as erro:

        print(f"\nErro no filtro de stock: {erro}")

        return []