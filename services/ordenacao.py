
# =====================================
# BUBBLE SORT
# =====================================
def bubble_sort_preco(lista_produtos):

    n = len(lista_produtos)

    for i in range(n):

        for j in range(0, n - i - 1):

            if lista_produtos[j].preco > lista_produtos[j + 1].preco:

                temp = lista_produtos[j]

                lista_produtos[j] = lista_produtos[j + 1]

                lista_produtos[j + 1] = temp

    print("\nProdutos ordenados por preço!")


# =====================================
# SELECTION SORT
# =====================================
def selection_sort_nome(lista_produtos):

    n = len(lista_produtos)

    for i in range(n):

        menor = i

        for j in range(i + 1, n):

            if lista_produtos[j].nome.lower() < lista_produtos[menor].nome.lower():

                menor = j

        temp = lista_produtos[i]

        lista_produtos[i] = lista_produtos[menor]

        lista_produtos[menor] = temp

    print("\nProdutos ordenados por nome!")
