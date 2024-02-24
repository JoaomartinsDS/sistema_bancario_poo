from abc import ABC,abstractclassmethod
from datetime import datetime

class Cliente:
    def __init__(self,endereco) :
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(conta,transacao):
        transacao.registrar(conta)
    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco,cpf,data_nascimento,nome):
        super().__init__(endereco)
        cpf = cpf
        data_nascimento = data_nascimento
        nome = nome

class Conta:
    def __init__(self,numero,cliente) -> None:
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._agencia = "0001"
        self._historico = Historico()
    @abstractclassmethod
    def nova_conta(cls,cliente,numero):
        return cls(cliente,numero)
    @property
    def numero(self):
        return self._numero
    @property
    def cliente(self):
        return self._cliente
    @property
    def saldo(self):
        return self._saldo
    @property
    def agencia(self):
        return self._agencia
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        if excedeu_saldo:
            print("\nOperação falhou, você não possui saldo suficiente para o saque!")
        elif valor > 0:
            self._saldo -= valor
            print("\n Saque realizado com sucesso!")
            return True
        else :
            print("Valor informado é inválido!")
        return False
    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
        else:
            print("Valor inválido!")
            return False
        return True


class Historico:
    def __init__(self):
        self._transacoes = []
    @property
    def transacoes(self):
        return self._transacoes
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %H:%M:%S"),
            }
        )

class transacao(ABC):
    @abstractclassmethod
    @property
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self,conta):
        pass

class Saque(transacao):
    def __init__(self,valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self):
        sucesso_transacao = Conta.sacar(self.valor)
        if sucesso_transacao:
            Conta.historico

