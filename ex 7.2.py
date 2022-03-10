class Kletka:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return Kletka(self.quantity + other.quantity)

    def __str__(self):
        return f'Количество клеток {self.quantity * "*"}'

    def __sub__(self, other):
        return self.quantity - other.quantity

    def __mul__(self, other):
        return Kletka(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Kletka(round(self.quantity // other.quantity))


kletka1 = Kletka(10)
kletka2 = Kletka(5)
print(kletka1)
print(kletka1 - kletka2)
print(kletka1 * kletka2)