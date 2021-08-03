

import turtle

wn = turtle.Screen()
wn.title('TrafficLights with Classes by Fridlyand Analytics')
wn.bgcolor('black')


class TrafficLight():
    def __init__(self, x, y):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed()
        self.pen.color("yellow")
        self.pen.goto(x-30, y+60)
        self.pen.pendown()
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.color = ""

        self.red_light = turtle.Turtle()
        self.yellow_light = turtle.Turtle()
        self.green_light = turtle.Turtle()

        self.red_light.speed(0)
        self.yellow_light.speed(0)
        self.green_light.speed(0)

        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")

        self.red_light.shape('circle')
        self.yellow_light.shape('circle')
        self.green_light.shape('circle')

        self.red_light.penup()
        self.yellow_light.penup()
        self.green_light.penup()

        self.red_light.goto(x, y+40)
        self.yellow_light.goto(x, y)
        self.green_light.goto(x, y-40)

    def running(self, color):

        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")
        if color == "red":
            self.red_light.color('red')
            self.color = "red"
        elif color == "yellow":
            self.yellow_light.color('yellow')
            self.color = "yellow"
        elif color == "green":
            self.green_light.color('green')
            self.color = 'green'
        else:
            print("Error: Unknown color {}".format(color))

    def timer(self):
        if self.color == 'red':
            self.running('green')
            wn.ontimer(self.timer, 7000)
        elif self.color == 'yellow':
            self.running("red")
            wn.ontimer(self.timer, 2000)
        elif self.color == "green":
            self.running("yellow")
            wn.ontimer(self.timer, 1000)
            # elif self.__color == 'yellow':
            #      self.running("red")
            #      wn.ontimer(self.timer, 2000)


trafficlight1 = TrafficLight(0, 0)
trafficlight1.running('red')
trafficlight1.timer()


trafficlight2 = TrafficLight(-100, 0)
trafficlight2.running('yellow')
trafficlight2.timer()

trafficlight3 = TrafficLight(100, 0)
trafficlight3.running('green')
trafficlight3.timer()

trafficlight4 = TrafficLight(200, 0)
trafficlight4.running('red')
trafficlight4.timer()

trafficlight5 = TrafficLight(-200, 0)
trafficlight5.running('yellow')
trafficlight5.timer()
wn.mainloop()
