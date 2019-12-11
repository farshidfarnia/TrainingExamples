class Point:
    def move(self):
        print(f'Move object to point {x_coordinates}')
    def draw(self):
        print(f"Draw the rectangle with this coordinate:{rectangle_coordinate}")


x_coordinates = 1.16
rectangle_coordinate = ["0,0", "0,2", "2,4", "2,0"]
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'Hi {self.name}🤩 Welcome')


john = Person("John Smith", 25)
print(john.name, john.age)
john.talk()