class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def eh_valido(self):
        a, b, c = self.a, self.b, self.c
        if a <= 0 or b <= 0 or c <= 0:
            return False
        return a + b > c and a + c > b and b + c > a

    def classificar(self):
        if not self.eh_valido():
            return "invalido"
        if self.a == self.b == self.c:
            return "equilatero"
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        return "escaleno"
