from datetime import datetime

from services.crud import adicionar_produto
from services.crud import listar_produtos
from services.crud import editar_produto
from services.crud import eliminar_produto

from services.estatisticas import mostrar_estatisticas

from services.ordenacao import bubble_sort_preco
from services.ordenacao import selection_sort_nome

from services.pesquisa import pesquisa_linear
from services.pesquisa import pesquisa_binaria

from services.json_manager import carregar_produtos
from services.json_manager import guardar_produtos

from services.produtos_exemplo import carregar_produtos_exemplo
from services.authentication import login

from services.email_stock import gerar_email_stock
from services.exportacao import menu_exportacao


# BYTE TECH
# Sistema de Gestão de Loja Informática


# lista principal

lista_produtos = carregar_produtos()


# login

acesso = login()

if acesso is False:

    print("\nAcesso negado.")
    exit()


# menu principal

while True:

    # data e hora

    data_atual = datetime.now()

    data_formatada = data_atual.strftime(
        "%d-%m-%Y %H:%M:%S"
    )

    print("\n========== BYTE TECH ==========")

    print(f"Data e Hora: {data_formatada}")


    # alertas de stock

    alertas = []

    for produto in lista_produtos:


        # produtos caros

        if produto.preco >= 300:

            if produto.stock == 0:

                alertas.append(

                    f"{produto.nome} -> QUEBRA DE STOCK"

                )

            elif produto.stock <= 2:

                alertas.append(

                    f"{produto.nome} -> ENCOMENDAR STOCK"

                )


        # produtos normais

        else:

            if produto.stock == 0:

                alertas.append(

                    f"{produto.nome} -> QUEBRA DE STOCK"

                )

            elif produto.stock < 5:

                alertas.append(

                    f"{produto.nome} -> STOCK BAIXO"

                )


    # mostrar alertas

    if len(alertas) > 0:

        print("\n⚠ ALERTA DE STOCK ⚠")

        for alerta in alertas:

            print(alerta)


    print("\n1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Editar produto")
    print("4 - Eliminar produto")
    print("5 - Pesquisa linear")
    print("6 - Estatísticas")
    print("7 - Ordenar produtos")
    print("8 - Guardar produtos")
    print("9 - Pesquisa binária")
    print("10 - Carregar produtos exemplo")
    print("11 - Gerar email stock baixo")
    print("12 - Exportação de dados")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")


    # adicionar produto

    if opcao == "1":

        try:

            adicionar_produto(lista_produtos)

        except Exception as erro:

            print(f"\nErro ao adicionar produto: {erro}")


    # listar produtos

    elif opcao == "2":

        try:

            listar_produtos(lista_produtos)

        except Exception as erro:

            print(f"\nErro ao listar produtos: {erro}")


    # editar produto

    elif opcao == "3":

        try:

            editar_produto(lista_produtos)

        except Exception as erro:

            print(f"\nErro ao editar produto: {erro}")


    # eliminar produto

    elif opcao == "4":

        try:

            eliminar_produto(lista_produtos)

        except Exception as erro:

            print(f"\nErro ao eliminar produto: {erro}")


    # pesquisa linear

    elif opcao == "5":

        try:

            pesquisa_linear(lista_produtos)

        except Exception as erro:

            print(f"\nErro na pesquisa: {erro}")


    # estatísticas

    elif opcao == "6":

        try:

            mostrar_estatisticas(lista_produtos)

        except Exception as erro:

            print(f"\nErro ao mostrar estatísticas: {erro}")


    # ordenação

    elif opcao == "7":

        print("\n===== ORDENAÇÃO =====")
        print("1 - Bubble Sort (Preço)")
        print("2 - Selection Sort (Nome)")

        opcao_ordenar = input("\nEscolha uma opção: ")

        print("\n===== ORDEM =====")
        print("1 - Crescente")
        print("2 - Decrescente")

        opcao_ordem = input("\nEscolha uma ordem: ")


        # definir ordem

        if opcao_ordem == "1":

            ordem = "crescente"

        elif opcao_ordem == "2":

            ordem = "decrescente"

        else:

            print("\nOrdem inválida.")
            continue


        # bubble sort

        if opcao_ordenar == "1":

            try:

                bubble_sort_preco(
                    lista_produtos,
                    ordem
                )

            except Exception as erro:

                print(f"\nErro na ordenação: {erro}")


        # selection sort

        elif opcao_ordenar == "2":

            try:

                selection_sort_nome(
                    lista_produtos,
                    ordem
                )

            except Exception as erro:

                print(f"\nErro na ordenação: {erro}")


        # opção inválida

        else:

            print("\nOpção inválida.")


    # guardar produtos

    elif opcao == "8":

        try:

            guardar_produtos(lista_produtos)

        except Exception as erro:

            print(f"\nErro ao guardar produtos: {erro}")


    # pesquisa binária

    elif opcao == "9":

        try:

            pesquisa_binaria(lista_produtos)

        except Exception as erro:

            print(f"\nErro na pesquisa binária: {erro}")


    # carregar produtos exemplo

    elif opcao == "10":

        try:

            carregar_produtos_exemplo(lista_produtos)

        except Exception as erro:

            print(f"\nErro ao carregar produtos exemplo: {erro}")


    # gerar email stock baixo

    elif opcao == "11":

        try:

            gerar_email_stock(lista_produtos)

        except Exception as erro:

            print(f"\nErro ao gerar email: {erro}")


    # exportação de dados

    elif opcao == "12":

        try:

            menu_exportacao(lista_produtos)

        except Exception as erro:

            print(f"\nErro na exportação: {erro}")


    # sair

    elif opcao == "0":

        guardar = input(
            "\nDeseja guardar os produtos antes de sair? (s/n): "
        ).lower()

        if guardar == "s":

            try:

                guardar_produtos(lista_produtos)

            except Exception as erro:

                print(f"\nErro ao guardar produtos: {erro}")


        print("\nA sair do sistema...")
        break


    # opção inválida

    else:

        print("\nOpção inválida.")