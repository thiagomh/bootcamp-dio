menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair    

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

      opcao = input(menu)

      if opcao == 'd':
            deposito = float(input("Qual valor deseja depositar"))
            if deposito > 0:
                  saldo += deposito
                  extrato += f"Depósito: valor de R${deposito:.2f}\n"
            else:
                  print("Valor inválido.")

      elif opcao == 's':
            saque = float(input("Qual valor deseja sacar: "))

            if saque > 500:
                  print("O valor máximo de saque é de R$ 500,00")
                  continue

            if numero_saques >= LIMITE_SAQUES:
                  print("Número de saques diários atingido")
                  continue

            if saque > saldo:
                  print("Você não possui saldo suficiente")
                  continue

            if saque > 0:
                  saldo -= saque
                  numero_saques += 1
                  extrato += f"Saque: valor de R${saque}\n"
            else:
                  print("Valor inválido.")

      elif opcao == 'e':
            print("Não foram realizadas transações." if not extrato else extrato)

      elif opcao == 'q':
            print("Encerrando...")
            break

      else:
            print("Operação Inválida.")