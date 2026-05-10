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

# LISTA PRINCIPAL
lista_produtos = carregar_produtos()

# MENU PRINCIPAL
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
    print("9 - Pesquisa Binária")
    print("10 - Carregar produtos exemplo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # ADICIONAR PRODUTO
    if opcao == "1":

        adicionar_produto(lista_produtos)

    # LISTAR PRODUTOS
    elif opcao == "2":

        listar_produtos(lista_produtos)

    # EDITAR PRODUTO
    elif opcao == "3":

        editar_produto(lista_produtos)

    # ELIMINAR PRODUTO
    elif opcao == "4":

        eliminar_produto(lista_produtos)

    # PESQUISA LINEAR
    elif opcao == "5":

        pesquisa_linear(lista_produtos)

    # ESTATÍSTICAS
    elif opcao == "6":

        mostrar_estatisticas(lista_produtos)

    # ORDENAÇÃO
    elif opcao == "7":

        print("\n=== ORDENAÇÃO ===")
        print("1 - Bubble Sort (Preço)")
        print("2 - Selection Sort (Nome)")

        opcao_ordenar = input("Escolha uma opção: ")

        if opcao_ordenar == "1":

            bubble_sort_preco(lista_produtos)

        elif opcao_ordenar == "2":

            selection_sort_nome(lista_produtos)

        else:

            print("\nOpção inválida.")

    # GUARDAR PRODUTOS
    elif opcao == "8":

        guardar_produtos(lista_produtos)

    # PESQUISA BINÁRIA
    elif opcao == "9":

        pesquisa_binaria(lista_produtos)

    # PRODUTOS EXEMPLO
    elif opcao == "10":

        carregar_produtos_exemplo(lista_produtos)

    # SAIR
    elif opcao == "0":

        guardar = input(
            "\nDeseja guardar os produtos antes de sair? (s/n): "
        ).lower()

        if guardar == "s":

            guardar_produtos(lista_produtos)

        print("\nA sair do sistema...")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("\nOpção inválida.")