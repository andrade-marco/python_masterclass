class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('We are flying, it is great')
        elif self.ratio == 1:
            print('This is hard, but I am flying')
        else:
            print('I cannot fly, I will walk instead')


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print('Waddle, waddle, waddle')

    def swim(self):
        print('Come on in, the water is lovely')

    def quack(self):
        print('Quack, quack!')

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print('Waddle, waddle, I waddle too')

    def swim(self):
        print('Come on in, but it is a bit chilly this far south')

    def quack(self):
        print('Are you having a laugh? I am a penguin')

    def aviate(self):
        print('I won the lottery and bought a learjet')


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck):
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError('Cannot add duck, are you sure it is not a ' + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("This 'duck' cannot fly...")
                problem = e

        if problem:
            raise problem

# Testing
def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    donald = Duck()
    percy = Penguin()
    test_duck(donald)
    test_duck(percy)
