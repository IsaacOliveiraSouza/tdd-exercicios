import re

NOME_INVALIDO = "O nome deve ter ao menos 2 partes compostas apenas por letras"
IDADE_INVALIDA = "A idade deve estar entre 1 e 200"
SEM_EMAIL = "A pessoa deve ter ao menos um email"
EMAIL_INVALIDO = "Email em formato invalido"

FORMATO_EMAIL = re.compile(r"^[^@\s]+@[^@\s.]+(\.[^@\s.]+)+$")


class Email:
    def __init__(self, name):
        self.name = name


class Person:
    def __init__(self, name, age, emails=None):
        self.name = name
        self.age = age
        self.emails = emails or []


class PersonDAO:
    def is_valid_to_include(self, person):
        erros = []
        if not self._nome_valido(person.name):
            erros.append(NOME_INVALIDO)
        if not self._idade_valida(person.age):
            erros.append(IDADE_INVALIDA)
        if not person.emails:
            erros.append(SEM_EMAIL)
        elif not all(self._email_valido(email) for email in person.emails):
            erros.append(EMAIL_INVALIDO)
        return erros

    def _nome_valido(self, nome):
        if not isinstance(nome, str):
            return False
        partes = nome.split()
        return len(partes) >= 2 and all(parte.isalpha() for parte in partes)

    def _idade_valida(self, idade):
        return isinstance(idade, int) and 1 <= idade <= 200

    def _email_valido(self, email):
        return isinstance(email.name, str) and FORMATO_EMAIL.match(email.name) is not None
