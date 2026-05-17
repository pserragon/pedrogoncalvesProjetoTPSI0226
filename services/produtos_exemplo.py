
# PRODUTOS EXEMPLO BYTE TECH

from models.produto import Produto


# CARREGAR PRODUTOS EXEMPLO
def carregar_produtos_exemplo(lista_produtos):

    try:

        # evitar duplicados

        if len(lista_produtos) > 0:

            print(

                "\nJá existem produtos carregados."

            )

            return


        produtos = [

            # CPUs
            Produto(1, "Ryzen 5 7600X", 249.99, 8, "CPU", "AMD", "amd@bytetech.pt", "912345678"),
            Produto(2, "Ryzen 7 7800X3D", 429.99, 2, "CPU", "AMD", "amd@bytetech.pt", "912345678"),
            Produto(3, "Ryzen 9 7950X", 699.99, 1, "CPU", "AMD", "amd@bytetech.pt", "912345678"),
            Produto(4, "Intel i5 14600K", 329.99, 5, "CPU", "Intel", "intel@bytetech.pt", "913456789"),
            Produto(5, "Intel i7 14700K", 469.99, 3, "CPU", "Intel", "intel@bytetech.pt", "913456789"),
            Produto(6, "Intel i9 14900K", 749.99, 1, "CPU", "Intel", "intel@bytetech.pt", "913456789"),
            Produto(7, "Ryzen 5 5600", 139.99, 10, "CPU", "AMD", "amd@bytetech.pt", "912345678"),
            Produto(8, "Ryzen 7 5800X", 259.99, 4, "CPU", "AMD", "amd@bytetech.pt", "912345678"),
            Produto(9, "Intel i3 14100F", 129.99, 12, "CPU", "Intel", "intel@bytetech.pt", "913456789"),
            Produto(10, "Intel i5 12400F", 179.99, 7, "CPU", "Intel", "intel@bytetech.pt", "913456789"),

            # GPUs
            Produto(11, "RTX 4060", 329.99, 6, "GPU", "Nvidia", "nvidia@bytetech.pt", "914567890"),
            Produto(12, "RTX 4070", 629.99, 3, "GPU", "Nvidia", "nvidia@bytetech.pt", "914567890"),
            Produto(13, "RTX 4070 Ti", 849.99, 2, "GPU", "Nvidia", "nvidia@bytetech.pt", "914567890"),
            Produto(14, "RTX 4080", 1299.99, 1, "GPU", "Nvidia", "nvidia@bytetech.pt", "914567890"),
            Produto(15, "RTX 4090", 1999.99, 0, "GPU", "Nvidia", "nvidia@bytetech.pt", "914567890"),
            Produto(16, "RX 7600", 299.99, 8, "GPU", "AMD", "amd@bytetech.pt", "912345678"),
            Produto(17, "RX 7700 XT", 499.99, 4, "GPU", "AMD", "amd@bytetech.pt", "912345678"),
            Produto(18, "RX 7800 XT", 589.99, 2, "GPU", "AMD", "amd@bytetech.pt", "912345678"),
            Produto(19, "RX 7900 XT", 899.99, 1, "GPU", "AMD", "amd@bytetech.pt", "912345678"),
            Produto(20, "RX 7900 XTX", 1099.99, 0, "GPU", "AMD", "amd@bytetech.pt", "912345678")

        ]

        for produto in produtos:

            lista_produtos.append(produto)

        print(

            "\nProdutos exemplo carregados com sucesso!"

        )

    except Exception as erro:

        print(

            f"\nErro ao carregar produtos exemplo: {erro}"

        )