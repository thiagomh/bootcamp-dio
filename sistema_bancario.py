menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar usuário
[c] Criar conta
[pc] Exibir contas
[q] Sair    

=> '''

def depositar(valor: float, saldo: float, extrato: str, /):
      if valor > 0:
            saldo += valor
            extrato += f"Depósito: valor de R${valor:.2f}\n"
      else:
            print("Valor inválido.\n")
      
      return saldo, extrato

def sacar(valor: float, saldo: float, extrato: str, limite, num_saques, limite_saques):
      if valor > limite:
            print("O valor máximo de saque é de R$ 500,00")
            return saldo, extrato, num_saques

      if num_saques >= limite_saques:
            print("Número de saques diários atingido")
            return saldo, extrato, num_saques

      if valor > saldo:
            print("Você não possui saldo suficiente")
            return saldo, extrato, num_saques

      if valor > 0:
            saldo -= valor
            num_saques += 1
            extrato += f"Saque: valor de R${valor}\n"
            print("Saque realizado.\n")
      else:
            print("Valor inválido.")

      return saldo, extrato, num_saques

def exibir_extrato(saldo: float, /, *, extrato: str):
      print(f"-------Saldo atual: {saldo}-------")
      print("Não foram realizadas transações." if not extrato else extrato)
      return

def criar_usuario(usuarios):
      cpf = str(input("Informe seu CPF: (somente números)"))

      for usuario in usuarios: 
            if cpf == usuario['cpf']:
                  print("Esse cpf já está cadastrado")
                  return
      
      nome = input("Informe seu nome completo")
      data_nasc = input("Informe sua data de nascimento (DD/MM/AAAA)")
      endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado)")

      novo_usuario = {"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco}

      usuarios.append(novo_usuario)

      print("Usuário cadastrado com sucesso")

def criar_conta(usuarios, contas, num_agencia, num_conta):
      cpf = str(input("Informe o cpf do usuário: (somente números)"))

      for usuario in usuarios:
            if cpf == usuario['cpf']:
                  nova_conta = {"usuario": usuario, "numero_agencia":num_agencia, "numero_conta":num_conta}
                  contas.append(nova_conta)
                  print("Conta criada com sucesso!")
                  return
      else:
            print("Usuário não cadastrado.")

def main():
      LIMITE_SAQUES = 3
      NUMERO_AGENCIA = "0001"
      saldo = 0
      limite = 500
      extrato = ""
      numero_saques = 0
      usuarios = []
      contas = []
      
      while True:

            opcao = input(menu)

            if opcao == 'd':
                  deposito = float(input("Qual valor deseja depositar"))
                  
                  saldo, extrato = depositar(deposito, saldo, extrato)

            elif opcao == 's':
                  saque = float(input("Qual valor deseja sacar: "))

                  saldo, extrato, numero_saques = sacar(saldo=saldo, 
                                                        valor=saque,
                                                        extrato=extrato,
                                                        limite=limite,
                                                        num_saques=numero_saques,
                                                        limite_saques=LIMITE_SAQUES)
                  
            elif opcao == 'e':
                  exibir_extrato(saldo, extrato=extrato)

            elif opcao == 'u':
                  criar_usuario(usuarios)

            elif opcao == 'c':
                  numero_conta = len(contas) + 1
                  criar_conta(usuarios, contas, NUMERO_AGENCIA, numero_conta)

            elif opcao == 'pc':
                  for conta in contas:
                        print(f"Numero da conta: {conta['numero_conta']}")
                        print(f"Usuário: {conta['usuario']['nome']}")
                        print(f"Numero da Agencia {conta['numero_agencia']}\n\n")


            elif opcao == 'q':
                  print("Encerrando...")
                  break

            else:
                  print("Operação Inválida.")

main()