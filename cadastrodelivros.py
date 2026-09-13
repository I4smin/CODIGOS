class Livro:
    def __init__(self, titulo, autor, preco, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.quantidade = quantidade

    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print("-" * 30)


livros = []

while True:
    print("\n--- CADASTRO DE LIVRO ---")

    titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")

    preco = float(input("Digite o preço: R$ "))
    quantidade = int(input("Digite a quantidade: "))

    livro = Livro(titulo, autor, preco, quantidade)

    livros.append(livro)

    continuar = input("\nDeseja cadastrar outro livro? (s/n): ")

    if continuar.lower() != "s":
        break

print("\n===== LIVROS CADASTRADOS =====")

for livro in livros:
    livro.exibir_dados()
