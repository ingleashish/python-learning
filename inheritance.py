class Animal():

    def __init__(self):
        print("Animal instance created")

    def who_am_i(self):
        print("I'm Animal")

    def eat(self):
        print("Animal eating...!")

class Dog(Animal):

    def __init__(self, name=""):
        Animal.__init__(self)
        self.name = name;
        print("Dog instance created")

    def who_am_i(self):
        print("I am Dog")

    def bark(self):
        print("Dog is barking...!")

    def __str__(self):
        return "I am Dog name {}".format(self.name)

    

sam = Dog("Sam")
print(sam);

sam.who_am_i()
sam.eat()
sam.bark()
