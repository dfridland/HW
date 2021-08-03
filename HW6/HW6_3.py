class Worker:

    def __init__(self, name, surname, position, wages, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": wages, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
         return (f'{self.name} {self.surname}')


    def get_total_income(self):
        return sum(self._income.values())


p1 = Position("Eva", "Smith", "FD", 100000, 15000)
print(p1.get_full_name())
print(p1.get_total_income())
p2 = Position("Alan", "Clark", "PC", 85000, 10000)
print(p2.get_full_name())
print(p2.get_total_income())
p3 = Position("Anna", "Corselis", "PM", 800000, 10000)
print(p3.get_full_name())
print(p3.get_total_income())


