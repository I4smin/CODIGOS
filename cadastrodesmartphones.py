class Smartphone:

    # Método construtor
    def __init__(self, marca, armazenamento, cor, sistema_operacional,
                 preco, fabricante, ano_fabricacao):

        # Atributos de instância
        self.marca = marca
        self.armazenamento = armazenamento
        self.cor = cor
        self.sistema_operacional = sistema_operacional
        self.preco = preco
        self.fabricante = fabricante
        self.ano_fabricacao = ano_fabricacao

    # Método para exibir os dados do smartphone
    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Armazenamento: {self.armazenamento} GB")
        print(f"Cor: {self.cor}")
        print(f"Sistema Operacional: {self.sistema_operacional}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Ano de Fabricação: {self.ano_fabricacao}")
        print("-" * 40)


# Lista para armazenar os smartphones
smartphones = []


# Inicia o cadastro dos smartphones
while True:

    print("\n===== CADASTRO DE SMARTPHONE =====")

    # Solicita os dados ao usuário
    marca = input("Digite a marca: ")

    armazenamento = int(
        input("Digite o armazenamento em GB: ")
    )

    cor = input("Digite a cor: ")

    sistema_operacional = input(
        "Digite o sistema operacional: "
    )

    preco = float(
        input("Digite o preço: R$ ")
    )

    fabricante = input("Digite o fabricante: ")

    ano_fabricacao = int(
        input("Digite o ano de fabricação: ")
    )

    # Cria um objeto da classe Smartphone
    smartphone = Smartphone(
        marca,
        armazenamento,
        cor,
        sistema_operacional,
        preco,
        fabricante,
        ano_fabricacao
    )

    # Adiciona o objeto na lista
    smartphones.append(smartphone)

    # Pergunta se deseja cadastrar outro smartphone
    continuar = input(
        "\nDeseja cadastrar outro smartphone? (s/n): "
    )

    # Se a resposta for diferente de "s", encerra o while
    if continuar.lower() != "s":
        break


# Exibe todos os smartphones cadastrados
print("\n===== SMARTPHONES CADASTRADOS =====")

# Apresenta a quantidade de smartphones cadastrados
print(f"Quantidade de smartphones cadastrados: {len(smartphones)}")

print()

# Percorre a lista e exibe os dados de cada smartphone
for smartphone in smartphones:
    smartphone.exibir_dados()
