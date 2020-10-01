class Car(object):
    def __init__(self,model, year, price):
        self.model = model
        self.year = year
        self.price = price

class Supercar(Car):
    def cc_inc (self):
        self.cc = self.cc * 1.15

toyota = Car('Innova',2018,15000)
fortuner = Supercar('ToyotaFortunera',2020,25000)

fortuner.cc=1200
print(toyota.__dict__)
print(fortuner.__dict__)
fortuner.cc_inc()
print(fortuner.cc)
print()

class Employee(object):
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

dev_1 = Developer('fahim','ash',5000, 'python')
dev_2 = Developer('john','jak',9000, 'java')
print(dev_1.email)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)