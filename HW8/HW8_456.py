class Depot:
    def __init__(self, name):
        self.name = name
        self.my_dict = {}
        self.give_dict = {}

    def add_to_depot(self, eq):
       return self.my_dict.update({eq.eq_name(): (eq.name, eq.ser_num)})

       # print(f'Depot {self.name} received: {eq.name}, {eq.ser_num}')

    def send_to_dep(self, eq):

       return self.give_dict.update({eq.eq_name():(eq.name, eq.ser_num)})

       # print(f'Equipment to send: {eq.name}, {eq.ser_num}')
        # other.send_to_depot(eq)
    def depot_dict(self):

        print(f'Equipment at the Depot: {self.my_dict}')
        print(f'Equipment to leave the Depot: {self.give_dict}')

class Eq:
    def __init__(self, name, ser_num):
        self.name = name
        self.ser_num = ser_num
        self.group = self.__class__.__name__

    def eq_name(self):
            return f'{self.group}'

    # def __str__(self):
    #         return f'{self.name} {self.ser_num}'


class Printer(Eq):
    def __init__(self, name, ser_num, color):
        super().__init__(name, ser_num)
        self.color = color

    def __str__(self):
        return f'{self.name} {self.ser_num} {self.color}'

class Scaner(Eq):
    def __init__(self, name, ser_num, resolution):
        super().__init__(name, ser_num)
        self.resolution = resolution

    def __str__(self):
         return f'{self.name} {self.ser_num} {self.resolution}'

class Copier(Eq):
    def __init__(self, name, ser_num, speed):
        super().__init__(name, ser_num)
        self.speed = speed

    def __str__(self):
        return f'{self.name} {self.ser_num} {self.speed}'

depot1 = Depot('Main')
depot2 = Depot("Small")
printer = Printer("Canon-20", 233434, "color")
scaner = Scaner("HP", 234546, 33)
copier = Copier("epson-11", 65432, "4x")
print(printer)
depot1.add_to_depot(printer)
depot1.add_to_depot(scaner)
depot1.add_to_depot(copier)
depot2.add_to_depot(printer)
depot1.send_to_dep(printer)
depot1.send_to_dep(scaner)
depot1.depot_dict()