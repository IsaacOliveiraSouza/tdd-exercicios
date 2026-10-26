from enum import Enum


class Cargo(Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


class Funcionario:
    def __init__(self, nome, email, salario_base, cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo


class CalculadoraSalario:
    def calcular(self, funcionario):
        raise NotImplementedError
