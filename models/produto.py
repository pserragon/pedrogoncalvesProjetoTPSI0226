class Produto:
    def __init__(self, id, nome, preco, stock, categoria, empresa, email):
        # dados principais do produto

        self.id = id
        self.nome = nome
        self.preco = preco
        self.stock = stock
        self.categoria = categoria
        self.empresa = empresa
        self.email = email

    def mostrar(self):
        # mostra dados do produto

        print("ID:", self.id)
        print("Nome:", self.nome)
        print("Preço:", self.preco)
        print("Stock:", self.stock)
        print("Categoria:", self.categoria)
        print("Empresa:", self.empresa)
        print("Email:", self.email)
        print("----------------------")