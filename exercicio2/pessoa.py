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
        return []
