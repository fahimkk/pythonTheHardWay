class Parent(object):
    def override(self):
        print('PARENT override()')
    def implicit(self):
        print('PARENT implicit()')
    def altered(self):
        print('PAREN altered()')

class Child(Parent):
    def override(self):
        print('CHILD override()')
    def altered(self):
        print('CHILD Before Parent altered()')
        super(Child, self).altered()
        print('CHILD After Parent altered()')

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print('----')
dad.override()
son.override()
print('----')
dad.altered()
print()
son.altered()