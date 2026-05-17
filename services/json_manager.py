
# JSON MANAGER BYTE TECH

import json

from models.produto import Produto


# CARREGAR JSON
def carregar_produtos():

    lista_produtos = []

    try:

        with open(

            "data/produtos.json",
            "r",
            encoding="utf-8"

        ) as ficheiro:

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

        with open(

            "data/produtos.json",
            "w",
            encoding="utf-8"

        ) as ficheiro:

            json.dump([], ficheiro)

    except Exception as erro:

        print(f"\nErro ao carregar JSON: {erro}")

    return lista_produtos


# GUARDAR JSON
def guardar_produtos(lista_produtos):

    try:

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

        with open(

            "data/produtos.json",
            "w",
            encoding="utf-8"

        ) as ficheiro:

            json.dump(
                lista_json,
                ficheiro,
                indent=4,
                ensure_ascii=False
            )

        print("\nProdutos guardados com sucesso!")

    except Exception as erro:

        print(f"\nErro ao guardar JSON: {erro}")