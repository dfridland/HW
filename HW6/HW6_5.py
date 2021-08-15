class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start  to draw {self.title}')

class Pen(Stationary):
    def draw(self):
        print(f' Write a title: {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'Draw a heart under the title {self.title}')
class Handle(Stationary):
    def draw(self):
        print(f'Highlight the title: {self.title}')

stationary = Stationary("smart drawing")
stationary.draw()
pen = Pen("OOP")
pen.draw()

pencil = Pencil("I love you")
pencil.draw()
marker = Handle("It's a marker not a handle")
marker.draw()
