
# PESQUISA BYTE TECH

# pesquisa linear

def pesquisa_linear(lista_produtos):

    try:

        if len(lista_produtos) == 0:

            print("\nNenhum produto registado.")
            return

        nome_pesquisa = input(
            "\nNome do produto: "
        ).lower()

        encontrado = False

        for produto in lista_produtos:

            if produto.nome.lower() == nome_pesquisa:

                print("\n===== PRODUTO ENCONTRADO =====")

                produto.mostrar()

                encontrado = True


        if encontrado is False:

            print("\nProduto não encontrado.")

    except Exception as erro:

        print(f"\nErro na pesquisa linear: {erro}")


# pesquisa binária

def pesquisa_binaria(lista_produtos):

    try:

        if len(lista_produtos) == 0:

            print("\nNenhum produto registado.")
            return


        # ordenar lista por nome

        n = len(lista_produtos)

        for i in range(n):

            menor = i

            for j in range(i + 1, n):

                if (

                    lista_produtos[j].nome.lower()

                    <

                    lista_produtos[menor].nome.lower()

                ):

                    menor = j

            temp = lista_produtos[i]

            lista_produtos[i] = lista_produtos[menor]

            lista_produtos[menor] = temp


        print("\nLista ordenada por nome.")


        # pedir nome

        nome_procurado = input(

            "\nNome do produto: "

        ).lower()


        # pesquisa binária

        inicio = 0

        fim = len(lista_produtos) - 1

        encontrado = False


        while inicio <= fim:

            meio = (inicio + fim) // 2

            nome_meio = (

                lista_produtos[meio].nome.lower()

            )


            if nome_meio == nome_procurado:

                print("\n===== PRODUTO ENCONTRADO =====")

                lista_produtos[meio].mostrar()

                encontrado = True

                break


            elif nome_procurado < nome_meio:

                fim = meio - 1


            else:

                inicio = meio + 1


        if encontrado is False:

            print("\nProduto não encontrado.")

    except Exception as erro:

        print(f"\nErro na pesquisa binária: {erro}")