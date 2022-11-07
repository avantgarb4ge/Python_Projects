

# defining parent class
class Feline():
    # initializing attributes
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def bark(self):
        msg = "woof"
        return msg

class Shorthair(Feline):
    owner = "Gary"
    toys = "string"

    # super() inherits from parent class
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    # using same function from parent but altering for child
    def bark(self):
        msg = "arf"
        return msg

class RussianBlue(Feline):
    stray = True
    prey = "mouse"

    # super() inherits from parent class
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    # using same function from parent but altering for child
    def bark(self):
        msg = "Hi, I'm Paul!"
        return msg

if __name__ == "__main__":
    cat = Feline('Rudy', 4, 'brown')
    print(cat.name, cat.age, cat.color)
    print(cat.bark())

    kibble = Shorthair('Kibble', 1, 'calico')
    print(kibble.name, kibble.age, kibble.color)
    print(kibble.bark())

    paul = RussianBlue('Paul', 19, 'gray')
    print(paul.name, paul.age, paul.color)
    print(paul.bark())

    
    
