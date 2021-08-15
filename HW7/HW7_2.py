from abc import ABC, abstractmethod

class Outfit(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def fabric_metres(self):
        pass

class Coat(Outfit):
    def __init__(self, size):
        super().__init__()
        self.size = size
    @property
    def fabric_metres(self):
        return round(self.size / 6.5 + 0.5, 1)


class Suit(Outfit):
    def __init__(self, height):
        super().__init__()
        self.height = height
    @property
    def fabric_metres(self):
        return round((2 * self.height + 0.3) / 100, 1)



coat1 = Coat(40)
coat2 = Coat(38)
coat3 = Coat(44)
suit1 = Suit(175)

print(coat2.fabric_metres)
print(coat3.fabric_metres)
print(suit1.fabric_metres)
print(coat1.fabric_metres + coat2.fabric_metres + coat3.fabric_metres + suit1.fabric_metres)

