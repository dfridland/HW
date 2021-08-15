class ComplexNumber:
    def __init__(self, real_a, j=0):
        self.real_a = real_a
        self.j = j

    def __str__(self):
        return f'({str(self.real_a)} + {self.j}j)'

    def __add__(self, other):
        return ComplexNumber(self.real_a + other.real_a, self.j + other.j)

    def __mul__(self, other):
        return ComplexNumber((self.real_a * other.real_a) + (self.j * other.j),
                             (self.j * other.real_a) + (self.real_a * other.j))

x1 = ComplexNumber(2, 10)
x2 = ComplexNumber(3, 5)
x3 = ComplexNumber(5, 3)

print(x1 + x2)
print(x1 * x2)
print(x3 + x2)
print(x3 * x2)
