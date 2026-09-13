while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura (em metros): "))
    salario = float(input("Digite seu salário: R$ "))

    estudante = input("É estudante? (s/n): ")

    print("\n--- Dados informados ---")
    print("Nome:", nome)
    print("Idade:", idade, "anos")
    print("Altura:", altura, "m")
    print("Salário: R$", salario)

    if estudante.lower() == "s":
        print("Estudante: Sim")
    else:
        print("Estudante: Não")

    continuar = input("\nDeseja cadastrar outra pessoa? (s/n): ")

    if continuar.lower() != "s":
        break

print("\nPrograma encerrado!")
