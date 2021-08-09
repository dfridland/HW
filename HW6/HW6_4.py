class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"{self.name}'s speed is {self.speed}")
    def go(self):
        print(f"{self.name} is moving")
    def stop(self):
        print(f"{self.name} stops")
    def turn(self, direction):
        print(f'{self.name} turns {"left" if direction == 0 else "right"}')

class TownCar(Car):
    def show_speed(self):
           print(f'Your speed is over 60!' if self.speed > 60 else
                   f"{self.name}'s speed is {self.speed}")

class SportCar(Car):
    def show_speed(self):
        if self.name in ['Ferrari', "Lamborghini", "Aston-Martin", "McLaren"] and self.speed > 80:
            print(f'Who cares speed limit when you drive {self.name}?')
        elif self.name in ['Ferrari', "Lamborghini", "Aston-Martin", "McLaren"] and self.speed <= 80:
             print(f"Why own {self.name} if drive with {self.speed}, loser")
        else:
            print(f"{self.name}'s speed is {self.speed}")

class WorkCar(Car):
    def show_speed(self):
        print(f'Your speed is over 40!' if self.speed > 40 else
              f"{self.name}'s speed is {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__( speed, color, name, is_police)

towncar1 = TownCar(80, "blue", "BMW", False)
towncar1.show_speed()
towncar2 = TownCar(45, "grey", "Toyota", False)
towncar2.show_speed()
towncar2.go()
workcar1 = WorkCar(48, 'black', "Mercedes", False)
workcar1.show_speed()
workcar1.stop()
sportcar1 = SportCar(100, 'red', "Ferrari", False)
sportcar1.show_speed()
sportcar1.stop()
sportcar1.turn(0)
sportcar2 = SportCar(75, 'blue', "Lamborghini", False)
sportcar2.show_speed()
sportcar3 = SportCar(75, 'blue', "Mustang", False)
sportcar3.show_speed()
policecar = PoliceCar (90, "white", "Police", True)
policecar.show_speed()
policecar.turn(1)