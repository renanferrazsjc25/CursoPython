# Modulo que define as classes de Contas (Abstrata, Corrente, Poupança)

# Importa a classe base  Abstrata e o decorador para metodos Abstratos
from abc import ABC, abstractmethod

# Importa a classe datetime para registrar data e hora das transacoes
from datetime import datetime

# Importa exceçao personalizada para saldo insuficiente
from modulo_dsautilitarios.exceptions import SaldoInsuficienteError

# Define a classe Abstrata Conta, que serve com base para outros tipos de contas

class Conta(ABC):

    # Classe base Abstrata para contas bancarias, demonstra Heranca e Encapsulamento

    # Atributos de classe que calcula quantas contas foram criadas
    _total_contas = 0

    # Construtor da classe
    def __init__(self, numero: int, cliente):
        # Numero de conta (atributo protegido)
        self.numero = numero
        # Saldo da conta inicializando em 0.0 (Atributo protegido)
        self.saldo = 0.0
        # Referencia ap cliente dono da conta
        self.cliente = cliente
        # Lista para armazenar historico de transaçoes
        self._historico = []
        # Icrementa o total de contas criadas
        Conta._total_contas += 1

    # Propiedade para acessar o saldo de forma controlada
    @property
    def saldo(self):

        # Getter para saldo, permitindo acesso controlado
        return self.saldo

    # Metodo de classe para consultar o numero total de contas
    @classmethod
    def get_total_contas(cls):
        
        # Metodo de classes para obter o numero total de contas criadas
        return cls._total_contas
    
    # Metodo para realizar depositos
    def depositar(self, valor: float):

        # Adiciona um valor ao saldo da conta
        if valor >0:

            # Icrementa o saldo
            self.saldo += valor

            # Registra a transação no historio com data e hora
            self._historico.append((datetime.now(), f'Deposito de R${valor:.2f}'))
            print (f'Deposito de R$ {valor:.2f} realizado com sucesso')

        else:

            print ('Valor de deposito invalido')

    # Metodo abstrato que deve ser implementado pelas subclasses

    @abstractmethod
    def sacar(self, valor: float):

        pass

    # Metodo para exibir o extrato da conta
    def extrato(self):

        # Exibe o contrato da conta
        print (f'\n--- Extrato da Conta N° {self.numero} ---')
        print (f'Cliente {self._cliente.nome}')
        print (f'Saldo Atual: R$ {self.saldo:.2f}')
        print ('Historico de transaçoes')

        # Caso nao haja transaçoes realizadas
        if not self._historico:
            print ('Nenhuma transação registrada')

        # Percorre o historico e exibe cada transação
        for data, transacao in self._historico:
            print (f'- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transacao}')
        print ('--------------------------------------\n')
    
# Define a subclasse conta ContaCorrente
class ContaCorrente(Conta):
    # Subclasse que representa uma conta Corrente, demonstra Polimorfismo ao sobrescrever o metodo sacar

    def __init__(self, numero: int, cliente, limite: float = 500.00):

        # Chama o construtor da classe base
        super().__init_(numero, cliente)

        # Define o limite de cheque especial
        self.limite = limite

    # Implementação do metodo sacar com cheque especial
    def sacar(self, valor: float):

        # Permite saque utilizando o saldo da conta mais o limite do (cheque especial)
        if valor <= 0:
            print ('Valor de saque invalido')
            return
        # Calcula o saldo disponivel (saldo + limite)
        saldo_disponivel = self.saldo + self.limite

        # Caso o valor do saque ultrapasse o saldo disponível
        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficientes.")
        
        # Deduz o valor do saque do saldo
        self._saldo -= valor

        # Registra a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

        
# Define a subclasse ContaPoupanca
class ContaPoupanca(Conta):

    """Subclasse que representa uma conta poupança."""

    # Construtor da poupança, herda do construtor base
    def __init__(self, numero: int, cliente):
        super().__init__(numero, cliente)

    # Implementação do método sacar apenas com saldo disponível
    def sacar(self, valor: float):

        # Permite saque apenas se houver saldo suficiente na conta.
        if valor <= 0:
            print("Valor de saque inválido.")
            return

        # Verifica se há saldo suficiente
        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)
            
        # Deduz o valor do saldo
        self._saldo -= valor
        
        # Registra a transação no histórico
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")