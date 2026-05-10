import json

from models.produto import Produto


# CARREGAR JSON
def carregar_produtos():

    lista_produtos = []

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
                    item["email"],
                    item["telefone"]
                )

                lista_produtos.append(produto)

    except FileNotFoundError:

        print(
            "\nFicheiro JSON não encontrado. Será criado automaticamente."
        )

    return lista_produtos


# GUARDAR JSON
def guardar_produtos(lista_produtos):

    lista_json = []

    for produto in lista_produtos:

        lista_json.append({
            "id": produto.id,
            "nome": produto.nome,
            "preco": produto.preco,
            "stock": produto.stock,
            "categoria": produto.categoria,
            "empresa": produto.empresa,
            "email": produto.email,
            "telefone": produto.telefone
        })

    with open("dados/produtos.json", "w") as ficheiro:

        json.dump(
            lista_json,
            ficheiro,
            indent=4
        )

    print("\nProdutos guardados com sucesso!")