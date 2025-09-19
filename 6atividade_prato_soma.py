import os 
os.system("cls")

preco_total = 0

while True:
    print("""
    codigo \t prato \t\t\t valor
      1 \t picanha \t\t R$ 25
      2 \t lasanha \t\t R$ 20
      3 \t strgonoff \t\t R$ 18
      4 \t Bife Acebolado \t R$ 15
      5 \t Pão com ovo \t\t R$ 5
 """)

    opcao = int(input("digite o codigo da opcçao: "))
    

    match opcao:
     
        case 1:
            prato = "picanha"
            preco = 25
        case 2:
            prato = "lasanha"
            preco = 20
        case 3:
            prato = "Strogonoff"
            preco = 18
        case 4:
            prato = "Bife Acebolado"
            preco = 15
        case 5:
            preco = "Pão com ovo"
            preco = 5
        case _:
            print("opção inválida.")
            print("tente novamente...")
            preco = 0
    
    preco_total = preco_total + preco

    mais_pedidos = input("deseja fazer um novo pedido?\nUse S ou N para responder: ").upper

    if mais_pedidos =="N":
        break


print=("\n===RESTAURANTE===")
print( "total a pagar: {preco_total}")

    

