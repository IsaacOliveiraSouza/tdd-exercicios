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


REGRAS = {
    Cargo.DESENVOLVEDOR: (3000.0, 0.20, 0.10),
    Cargo.DBA: (2000.0, 0.25, 0.15),
    Cargo.TESTADOR: (2000.0, 0.25, 0.15),
    Cargo.GERENTE: (5000.0, 0.30, 0.20),
}


class CalculadoraSalario:
    def calcular(self, funcionario):
        limite, desconto_maior, desconto_menor = REGRAS[funcionario.cargo]
        salario = funcionario.salario_base
        desconto = desconto_maior if salario >= limite else desconto_menor
        return salario * (1 - desconto)
