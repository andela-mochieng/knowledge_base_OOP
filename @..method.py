class Test(object):
    name = 'Margie Rain... Sunday'

    @staticmethod
    def name():
        '''Static methods cannot access class variables, don't take self and the class doesn't need to be initiatied '''
        return 'margierain'

    @classmethod
    def get_name(cls):
        '''Methods that have @classmethod decorator above them take
        cls as a parameter that refers to the class (like self does)
        however you don't need to instantiate the class i.e
        (t = test() ) you call it like (Test.get_food)
        such method can access class variables eg '''
        return cls.food

    @property
    def test(self):
        '''similar to instance method however one doen't need to call the method ie t = Test()  then t.test '''
        return 'TDD is in progress'

    def age(self):
        return 20


print Test.name()  # @staticmethod
print Test.get_food()  # @classmethod

t = Test()
print t.test  # @property
print t.age()  # instance method
