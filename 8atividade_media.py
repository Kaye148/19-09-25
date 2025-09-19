import os
os.system("cls")

soma = 0
quantidade_notas = 0

while True:
    nota = float(input("informe a nota: "))
    if nota <=0:
        break
    else:
        quantidade_notas += 1
        soma += nota
media = soma / quantidade_notas

print(f"Media:{media}")
