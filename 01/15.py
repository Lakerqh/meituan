class Animal(object):
    def run(self):
        print('Animal is running ...')

class Dog(Animal):
    def run(self):
        print('Dog is running ...')
    
    def eat(self):
        print('Eating meat ...')

class Cat(Animal):
    pass

dog = Dog()
dog.run()
dog.eat()

print(isinstance(dog,Animal))