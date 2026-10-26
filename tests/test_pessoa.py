import pytest

from exercicio2.pessoa import Email, Person, PersonDAO

NOME_INVALIDO = "O nome deve ter ao menos 2 partes compostas apenas por letras"
IDADE_INVALIDA = "A idade deve estar entre 1 e 200"
SEM_EMAIL = "A pessoa deve ter ao menos um email"
EMAIL_INVALIDO = "Email em formato invalido"


@pytest.fixture
def dao():
    return PersonDAO()


def pessoa(name="Joao Silva", age=30, emails=None):
    if emails is None:
        emails = [Email("joao@email.com")]
    return Person(name, age, emails)


def test_pessoa_valida_nao_tem_erros(dao):
    assert dao.is_valid_to_include(pessoa()) == []


def test_nome_com_tres_partes_eh_valido(dao):
    assert dao.is_valid_to_include(pessoa(name="Maria Clara Souza")) == []


def test_nome_com_acento_eh_valido(dao):
    assert dao.is_valid_to_include(pessoa(name="José Conceição")) == []


@pytest.mark.parametrize("name", ["Joao", "", "   ", "Joao 123", "Joao Silva2", "Joao S1lva", None])
def test_nome_invalido(dao, name):
    assert NOME_INVALIDO in dao.is_valid_to_include(pessoa(name=name))


@pytest.mark.parametrize("age", [1, 100, 200])
def test_idade_dentro_do_intervalo(dao, age):
    assert dao.is_valid_to_include(pessoa(age=age)) == []


@pytest.mark.parametrize("age", [0, -5, 201, None])
def test_idade_fora_do_intervalo(dao, age):
    assert IDADE_INVALIDA in dao.is_valid_to_include(pessoa(age=age))


def test_sem_email(dao):
    assert SEM_EMAIL in dao.is_valid_to_include(pessoa(emails=[]))


@pytest.mark.parametrize("endereco", ["a@b.c", "joao.silva@empresa.com.br"])
def test_email_valido(dao, endereco):
    assert dao.is_valid_to_include(pessoa(emails=[Email(endereco)])) == []


@pytest.mark.parametrize("endereco", ["joao", "@email.com", "joao@.com", "joao@email.", "joao@email", "joao email@x.com", ""])
def test_email_invalido(dao, endereco):
    assert EMAIL_INVALIDO in dao.is_valid_to_include(pessoa(emails=[Email(endereco)]))


def test_um_email_invalido_entre_validos(dao):
    emails = [Email("joao@email.com"), Email("invalido")]
    assert EMAIL_INVALIDO in dao.is_valid_to_include(pessoa(emails=emails))


def test_acumula_todos_os_erros(dao):
    erros = dao.is_valid_to_include(Person("Joao", 0, []))
    assert erros == [NOME_INVALIDO, IDADE_INVALIDA, SEM_EMAIL]
