
import json
import re

from models.produto import Produto

# =====================================
# LISTA PRINCIPAL
# =====================================
lista_produtos = []

# =====================================
# CARREGAR JSON
# =====================================
try:

    with open("dados/produtos.json", "r") as ficheiro:

        dados = json.load(ficheiro)

        for item in dados:

            produto = Produto(
                item["id"],
                item["nome"],
                item["preco"],
                item["stock"],
                item["categoria"],
                item["empresa"],
                item["email"]
            )

            lista_produtos.append(produto)

except FileNotFoundError:

    print("\nFicheiro JSON não encontrado. Será criado automaticamente.")

# =====================================
# MENU PRINCIPAL
# =====================================
while True:

    print("\n=== BYTE TECH ===")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Editar produto")
    print("4 - Eliminar produto")
    print("5 - Pesquisar produto")
    print("6 - Estatísticas")
    print("7 - Ordenar produtos")
    print("8 - Guardar produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # =====================================
    # ADICIONAR PRODUTO
    # =====================================
    if opcao == "1":

        try:

            id = int(input("ID: "))
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            stock = int(input("Stock: "))
            categoria = input("Categoria: ")
            empresa = input("Empresa: ")

            # =====================================
            # REGEX EMAIL
            # =====================================
            email = input("Email: ")

            padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

            resultado = re.match(padrao, email)

            if resultado:

                print("\nEmail válido!")
                print("Match:", resultado.group())
                print("Posição:", resultado.span())

            else:

                print("\nEmail inválido!")
                continue

            produto = Produto(
                id,
                nome,
                preco,
                stock,
                categoria,
                empresa,
                email
            )

            lista_produtos.append(produto)

            print("\nProduto adicionado com sucesso!")

        except ValueError:

            print("\nERRO: Introduziu valores inválidos.")

    # =====================================
    # LISTAR PRODUTOS
    # =====================================
    elif opcao == "2":

        if len(lista_produtos) == 0:

            print("\nNenhum produto registado.")

        else:

            print("\n=== LISTA DE PRODUTOS ===")

            for produto in lista_produtos:

                produto.mostrar()

    # =====================================
    # EDITAR PRODUTO
    # =====================================
    elif opcao == "3":

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
                        print("0 - Voltar")

                        opcao_editar = input("Escolha uma opção: ")

                        # editar nome
                        if opcao_editar == "1":

                            produto.nome = input("Novo nome: ")

                            print("\nNome atualizado com sucesso!")

                        # editar preço
                        elif opcao_editar == "2":

                            produto.preco = float(input("Novo preço: "))

                            print("\nPreço atualizado com sucesso!")

                        # editar stock
                        elif opcao_editar == "3":

                            produto.stock = int(input("Novo stock: "))

                            print("\nStock atualizado com sucesso!")

                        # editar categoria
                        elif opcao_editar == "4":

                            produto.categoria = input("Nova categoria: ")

                            print("\nCategoria atualizada com sucesso!")

                        # editar empresa
                        elif opcao_editar == "5":

                            produto.empresa = input("Nova empresa: ")

                            print("\nEmpresa atualizada com sucesso!")

                        # editar email
                        elif opcao_editar == "6":

                            novo_email = input("Novo email: ")

                            padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"

                            resultado = re.match(padrao, novo_email)

                            if resultado:

                                produto.email = novo_email

                                print("\nEmail atualizado com sucesso!")
                                print("Match:", resultado.group())
                                print("Posição:", resultado.span())

                            else:

                                print("\nEmail inválido!")

                        # voltar
                        elif opcao_editar == "0":

                            break

                        else:

                            print("\nOpção inválida.")

            if encontrado == False:

                print("\nProduto não encontrado.")

        except ValueError:

            print("\nERRO: Introduziu valores inválidos.")

    # =====================================
    # ELIMINAR PRODUTO
    # =====================================
    elif opcao == "4":

        try:

            id_eliminar = int(input("ID do produto a eliminar: "))

            encontrado = False

            for produto in lista_produtos:

                if produto.id == id_eliminar:

                    lista_produtos.remove(produto)

                    print("\nProduto eliminado com sucesso!")

                    encontrado = True
                    break

            if encontrado == False:

                print("\nProduto não encontrado.")

        except ValueError:

            print("\nERRO: Introduziu valores inválidos.")

    # =====================================
    # PESQUISA LINEAR
    # =====================================
    elif opcao == "5":

        nome_pesquisa = input("Nome do produto: ")

        encontrado = False

        for produto in lista_produtos:

            if produto.nome.lower() == nome_pesquisa.lower():

                print("\n=== PRODUTO ENCONTRADO ===")

                produto.mostrar()

                encontrado = True

        if encontrado == False:

            print("\nProduto não encontrado.")

    # =====================================
    # ESTATÍSTICAS
    # =====================================
    elif opcao == "6":

        if len(lista_produtos) == 0:

            print("\nNenhum produto registado.")

        else:

            # produto mais caro
            produto_caro = lista_produtos[0]

            for produto in lista_produtos:

                if produto.preco > produto_caro.preco:

                    produto_caro = produto

            print("\n=== PRODUTO MAIS CARO ===")

            produto_caro.mostrar()

            # média de preços
            soma_precos = 0

            for produto in lista_produtos:

                soma_precos += produto.preco

            media = soma_precos / len(lista_produtos)

            print(f"\nMédia de preços: {media:.2f} €")

            # produtos com pouco stock
            print("\n=== PRODUTOS COM POUCO STOCK ===")

            encontrou_stock = False

            for produto in lista_produtos:

                if produto.stock <= 2:

                    produto.mostrar()

                    encontrou_stock = True

            if encontrou_stock == False:

                print("Nenhum produto com pouco stock.")

    # =====================================
    # ORDENAÇÃO
    # =====================================
    elif opcao == "7":

        print("\n=== ORDENAÇÃO ===")
        print("1 - Bubble Sort (Preço)")
        print("2 - Selection Sort (Nome)")

        opcao_ordenar = input("Escolha uma opção: ")

        # BUBBLE SORT
        if opcao_ordenar == "1":

            n = len(lista_produtos)

            for i in range(n):

                for j in range(0, n - i - 1):

                    if lista_produtos[j].preco > lista_produtos[j + 1].preco:

                        temp = lista_produtos[j]

                        lista_produtos[j] = lista_produtos[j + 1]

                        lista_produtos[j + 1] = temp

            print("\nProdutos ordenados por preço!")

        # SELECTION SORT
        elif opcao_ordenar == "2":

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

        else:

            print("\nOpção inválida.")

    # =====================================
    # GUARDAR JSON
    # =====================================
    elif opcao == "8":

        lista_json = []

        for produto in lista_produtos:

            lista_json.append({
                "id": produto.id,
                "nome": produto.nome,
                "preco": produto.preco,
                "stock": produto.stock,
                "categoria": produto.categoria,
                "empresa": produto.empresa,
                "email": produto.email
            })

        with open("dados/produtos.json", "w") as ficheiro:

            json.dump(lista_json, ficheiro, indent=4)

        print("\nProdutos guardados com sucesso!")

    # =====================================
    # SAIR
    # =====================================
    elif opcao == "0":

        print("\nA sair do sistema...")
        break

    # =====================================
    # OPÇÃO INVÁLIDA
    # =====================================
    else:

        print("\nOpção inválida.")