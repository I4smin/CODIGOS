produtos = []
contador = 1
total = 0

while contador <= 5:
    nome = input(f"Digite o nome do {contador}º produto: ")
    valor = float(input(f"Digite o valor do {contador}º produto: R$ "))

    produtos.append([nome, valor])
    total += valor

    contador += 1

mais_caro = max(produtos, key=lambda produto: produto[1])
mais_barato = min(produtos, key=lambda produto: produto[1])

print("\n--- RESULTADO ---")
print(f"Valor total: R$ {total:.2f}")
print(f"Produto mais caro: {mais_caro[0]} - R$ {mais_caro[1]:.2f}")
print(f"Produto mais barato: {mais_barato[0]} - R$ {mais_barato[1]:.2f}")
