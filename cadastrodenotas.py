notas = []
contador = 1

while contador <= 10:
    nota = float(input(f"Digite a {contador}ª nota: "))
    notas.append(nota)
    contador += 1

maior = max(notas)
menor = min(notas)
media = sum(notas) / len(notas)

print("\n--- RESULTADO DA TURMA ---")
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Média da turma:", media)

aprovados = 0
reprovados = 0

for nota in notas:
    if nota > 7:
        aprovados += 1
    elif nota < 6.9:
        reprovados += 1

print("Aprovados:", aprovados)
print("Reprovados:", reprovados)
