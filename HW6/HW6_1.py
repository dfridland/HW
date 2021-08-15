
from time import sleep

class TrafficLight:
    __color = " "
    def running(self):
        while True:
            print("Traffic light is red now")
            sleep(7)
            print("Traffic light is yellow now")
            sleep(2)
            print("Traffic light is green now")
            sleep(2)
            print("Traffic light is yellow now")
            sleep(2)
            return

t = TrafficLight()
t.running()

