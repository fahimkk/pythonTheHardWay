class Animal(object):
    def __init__(self,phylum):
        self.phylum = phylum
    
class Fish(Animal):
    def __init__(self, subPhylum):
        self.subPhylum = subPhylum

class Person (Animal):
    def __init__(self, name):
        self.name = name
        self.pet = None 

class Dog (Animal):
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

fa = Person('Fahim')
