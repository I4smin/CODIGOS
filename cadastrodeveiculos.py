# Cria a classe Veiculo
class Veiculo:

    # Método construtor
    def __init__(self, placa, modelo, marca, ano, cor):

        # Atributos de instância
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor

    # Método para exibir os dados do veículo
    def exibir_dados(self):
        print(f"Placa: {self.placa}")
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print("-" * 30)


# Lista para armazenar os veículos cadastrados
veiculos = []


# Inicia o cadastro dos veículos
while True:

    print("\n===== CADASTRO DE VEÍCULO =====")

    # Solicita os dados ao usuário
    placa = input("Digite a placa: ")
    modelo = input("Digite o modelo: ")
    marca = input("Digite a marca: ")
    ano = int(input("Digite o ano: "))
    cor = input("Digite a cor: ")

    # Cria um objeto da classe Veiculo
    veiculo = Veiculo(placa, modelo, marca, ano, cor)

    # Adiciona o objeto à lista
    veiculos.append(veiculo)

    # Pergunta se deseja cadastrar outro veículo
    continuar = input("\nDeseja cadastrar outro veículo? (s/n): ")

    # Se a resposta for diferente de "s", encerra o cadastro
    if continuar.lower() != "s":
        break


# Lista todos os veículos cadastrados
print("\n===== VEÍCULOS CADASTRADOS =====")

# Apresenta a quantidade de veículos cadastrados
print(f"Quantidade de veículos cadastrados: {len(veiculos)}")

print()

# Percorre a lista e exibe os dados de cada veículo
for veiculo in veiculos:
    veiculo.exibir_dados()
