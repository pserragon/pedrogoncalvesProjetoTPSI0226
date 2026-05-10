class Produto:

    def __init__(
        self,
        id,
        nome,
        preco,
        stock,
        categoria,
        empresa,
        email,
        telefone
    ):

        self.id = id
        self.nome = nome
        self.preco = preco
        self.stock = stock
        self.categoria = categoria
        self.empresa = empresa
        self.email = email
        self.telefone = telefone

    def mostrar(self):

        print(f"\nID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Stock: {self.stock}")
        print(f"Categoria: {self.categoria}")
        print(f"Empresa: {self.empresa}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print("-" * 30)