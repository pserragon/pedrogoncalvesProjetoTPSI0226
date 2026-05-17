
# ORDENAÇÃO BYTE TECH

# bubble sort por preço

def bubble_sort_preco(

    lista_produtos,
    ordem="crescente"

):

    try:

        if len(lista_produtos) == 0:

            print("\nNenhum produto registado.")
            return


        n = len(lista_produtos)

        for i in range(n):

            for j in range(0, n - i - 1):


                # crescente

                if ordem == "crescente":

                    if (

                        lista_produtos[j].preco

                        >

                        lista_produtos[j + 1].preco

                    ):

                        temp = lista_produtos[j]

                        lista_produtos[j] = lista_produtos[j + 1]

                        lista_produtos[j + 1] = temp


                # decrescente

                elif ordem == "decrescente":

                    if (

                        lista_produtos[j].preco

                        <

                        lista_produtos[j + 1].preco

                    ):

                        temp = lista_produtos[j]

                        lista_produtos[j] = lista_produtos[j + 1]

                        lista_produtos[j + 1] = temp


        print(

            f"\nProdutos ordenados por preço ({ordem})!"

        )


        # mostrar produtos

        for produto in lista_produtos:

            produto.mostrar()

            print("-" * 30)


    except Exception as erro:

        print(f"\nErro na ordenação Bubble Sort: {erro}")


# selection sort por nome

def selection_sort_nome(

    lista_produtos,
    ordem="crescente"

):

    try:

        if len(lista_produtos) == 0:

            print("\nNenhum produto registado.")
            return


        n = len(lista_produtos)

        for i in range(n):

            indice = i

            for j in range(i + 1, n):


                # crescente

                if ordem == "crescente":

                    if (

                        lista_produtos[j].nome.lower()

                        <

                        lista_produtos[indice].nome.lower()

                    ):

                        indice = j


                # decrescente

                elif ordem == "decrescente":

                    if (

                        lista_produtos[j].nome.lower()

                        >

                        lista_produtos[indice].nome.lower()

                    ):

                        indice = j


            temp = lista_produtos[i]

            lista_produtos[i] = lista_produtos[indice]

            lista_produtos[indice] = temp


        print(

            f"\nProdutos ordenados por nome ({ordem})!"

        )


        # mostrar produtos

        for produto in lista_produtos:

            produto.mostrar()

            print("-" * 30)


    except Exception as erro:

        print(f"\nErro na ordenação Selection Sort: {erro}")