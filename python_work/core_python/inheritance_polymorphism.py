class Animal: #base class
    def __init__(self):
        self.numberoflegs = 4

    def make_noise(self):
        pass



# Dog is a sub class of Animal
class Dog(Animal):
    # make_noise method override
    def make_noise(self):
        print "woof, woof!"




#Cat is a sub class of Animal
class Cat(Animal):
    # make_noise method override
    def make_noise(self):
        print "Meow, meow!"



"""
    Polymorphism in action any object that
    implements the make_noise method can be
    perated on by Talk. 
"""
class Talk:
    def to(self, animal):
        animal.make_noise()




if __name__ == '__main__':
    animal = Dog()
    animal.make_noise()
    animal = Cat()
    animal.make_noise()
    talk = Talk()
    talk.to(animal)
