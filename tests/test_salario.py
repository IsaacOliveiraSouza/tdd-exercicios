import pytest

from exercicio3.salario import CalculadoraSalario, Cargo, Funcionario


def calcular(cargo, salario_base):
    funcionario = Funcionario("Ana", "ana@email.com", salario_base, cargo)
    return CalculadoraSalario().calcular(funcionario)


@pytest.mark.parametrize("salario_base, esperado", [(5000.0, 4000.0), (3000.0, 2400.0), (2999.99, 2699.991), (1000.0, 900.0)])
def test_desenvolvedor(salario_base, esperado):
    assert calcular(Cargo.DESENVOLVEDOR, salario_base) == pytest.approx(esperado)


@pytest.mark.parametrize("salario_base, esperado", [(4000.0, 3000.0), (2000.0, 1500.0), (1999.99, 1699.9915), (1000.0, 850.0)])
def test_dba(salario_base, esperado):
    assert calcular(Cargo.DBA, salario_base) == pytest.approx(esperado)


@pytest.mark.parametrize("salario_base, esperado", [(4000.0, 3000.0), (2000.0, 1500.0), (1999.99, 1699.9915), (1000.0, 850.0)])
def test_testador(salario_base, esperado):
    assert calcular(Cargo.TESTADOR, salario_base) == pytest.approx(esperado)


@pytest.mark.parametrize("salario_base, esperado", [(8000.0, 5600.0), (5000.0, 3500.0), (4999.99, 3999.992), (2000.0, 1600.0)])
def test_gerente(salario_base, esperado):
    assert calcular(Cargo.GERENTE, salario_base) == pytest.approx(esperado)


def test_funcionario_guarda_os_dados():
    funcionario = Funcionario("Ana", "ana@email.com", 3000.0, Cargo.DBA)
    assert funcionario.nome == "Ana"
    assert funcionario.email == "ana@email.com"
    assert funcionario.salario_base == 3000.0
    assert funcionario.cargo is Cargo.DBA
