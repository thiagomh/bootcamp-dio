from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
      def __init__(self, endereco) -> None:
            self._endereco = endereco
            self._contas = []

      def realizar_transacao(self, conta, transacao):
            transacao.registrar(conta)

      def adicionar_conta(self, conta):
            self._contas.append(conta)

class Conta: 
      def __init__(self, numero: int, cliente: Cliente) -> None:
            self._saldo = 0
            self._numero = numero
            self._agencia = "0001"
            self._cliente = cliente
            self._historico = Historico()

      @classmethod
      def nova_conta(cls, cliente: Cliente, numero: int):
            return cls(numero, cliente)

      @property
      def saldo(self) -> float:
            return self._saldo
      
      def sacar(self, valor: float) -> bool:
           if valor <= 0 or valor > self._saldo:
                 return False
           else:
                 self._saldo -= valor
                 return True 

      def depositar(self, valor: float) -> bool:
            if valor > 0:
                  self._saldo += valor
                  return True
            else:
                  return False
            
      @property
      def numero(self) -> int:
            return self._numero

      @property      
      def agencia(self) -> str:
            return self._agencia
      
      @property
      def cliente(self) -> Cliente:
            return self._cliente
      
      @property
      def historico(self):
            return self._historico
      
class Transacao(ABC):
      @abstractproperty
      def valor(self):
            pass
       
      @abstractclassmethod
      def registrar(conta: Conta):
            pass

class Historico:
      def __init__(self) -> None:
            self._transacoes = []

      @property
      def transacoes(self):
            return self._transacoes
      
      def adicionar_transacao(self, transacao: Transacao): 
            trasacao = {
                  "tipo": transacao.__class__.__name__,
                  "valor": transacao.valor
            }
            self._transacoes.append(transacao)

class Deposito(Transacao):
      def __init__(self, valor) -> None:
            self._valor = valor

      @property
      def valor(self):
            return self._valor
      
      def registrar(self, conta):
            transacao_ocorreu = conta.depositar(self.valor)

            if transacao_ocorreu:
                  conta.historico.adicionar_transacao(self)

class Saque(Transacao):
      def __init__(self, valor) -> None:
            self._valor = valor

      @property
      def valor(self):
            return self._valor
      
      def registrar(self, conta):
            transacao_ocorreu = conta.sacar(self.valor)

            if transacao_ocorreu:
                  conta.historico.adicionar_transacao(self)

class PessoaFisica(Cliente):
      def __init__(self, endereco, nome, data_nascimento, cpf) -> None:
            super().__init__(endereco)
            self.nome = nome 
            self.data_nascimento = data_nascimento
            self.cpf = cpf

class ContaCorrente(Conta):
      def __init__(self, numero: int, cliente: Cliente, limite=500, limite_saques=3) -> None:
            super().__init__(numero, cliente)
            self.limite = limite
            self.limite_saques = limite_saques

      def sacar(self, valor: float) -> bool:
            num_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
            
            if valor > self.limite or num_saques == self.limite_saques: 
                  return False
            else:
                  return super().sacar(valor)