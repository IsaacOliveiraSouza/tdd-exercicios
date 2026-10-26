import pytest

from exercicio1.triangulo import Triangulo


def test_escaleno_valido():
    assert Triangulo(3, 4, 5).classificar() == "escaleno"


def test_isosceles_valido():
    assert Triangulo(5, 5, 3).classificar() == "isosceles"


def test_equilatero_valido():
    assert Triangulo(4, 4, 4).classificar() == "equilatero"


@pytest.mark.parametrize("a, b, c", [(5, 5, 3), (5, 3, 5), (3, 5, 5)])
def test_isosceles_permutacoes(a, b, c):
    assert Triangulo(a, b, c).classificar() == "isosceles"


def test_um_valor_zero():
    assert Triangulo(0, 4, 5).classificar() == "invalido"


def test_um_valor_negativo():
    assert Triangulo(-3, 4, 5).classificar() == "invalido"


def test_soma_de_dois_lados_igual_ao_terceiro():
    assert Triangulo(1, 2, 3).classificar() == "invalido"


@pytest.mark.parametrize("a, b, c", [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
def test_soma_igual_permutacoes(a, b, c):
    assert Triangulo(a, b, c).classificar() == "invalido"


def test_soma_de_dois_lados_menor_que_o_terceiro():
    assert Triangulo(1, 2, 5).classificar() == "invalido"


@pytest.mark.parametrize("a, b, c", [(1, 2, 5), (1, 5, 2), (2, 1, 5), (2, 5, 1), (5, 1, 2), (5, 2, 1)])
def test_soma_menor_permutacoes(a, b, c):
    assert Triangulo(a, b, c).classificar() == "invalido"


def test_tres_valores_zero():
    assert Triangulo(0, 0, 0).classificar() == "invalido"
