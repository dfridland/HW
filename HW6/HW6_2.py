class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def eq_weight(self, weight = 25, thickness = 5):
        return (f"Asphalt's weight is {self._length * self._width * weight * thickness } kg (equals "
                f"{self._length * self._width * weight * thickness / 1000} ton).")

r1 = Road(int(input("Enter a length:  ")), (int(input("Enter a width:  "))))
print(r1.eq_weight())

r2 = Road(int(input("Enter a length:  ")), (int(input("Enter a width:  "))))
print(r2.eq_weight())
