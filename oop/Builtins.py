class Kettle(object):

    power_source = 'electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle('Kenwood', 8.99)
hamilton = Kettle('Hamilton', 14.55)
hamilton.switch_on()
print('Models: {}, {} | {}, {}'.format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print('Models: {0.make}, {0.price}, {0.on} | {1.make}, {1.price} | {1.on}'.format(kenwood, hamilton))

Kettle.switch_on(kenwood)
print('Models: {0.make}, {0.price}, {0.on} | {1.make}, {1.price} | {1.on}'.format(kenwood, hamilton))

kenwood.power = 1.5
print(kenwood.power)
