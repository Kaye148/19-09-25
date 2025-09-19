import os
os.system

soma = 0
quantidades_notas = 0

while True:
    nota = float(input("digite uma nota: "))
    quantidades_notas += 1
    soma += nota
    #soma = soma + nota
    resposta = input("deseja inserir uma nota? \nUse S ou N: ").lower()
    if resposta == "n":
        break

media = soma / quantidades_notas

print(f"\nMédia: {media}")
