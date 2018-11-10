import random

# Enemy Superclass
class Enemy(object):
    """Superclass for Enemies"""

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print('I took {} points damage, and have {} left'.format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print('{0.name} lost a life.'.format(self))
            else:
                print('{0.name} is dead...'.format(self))
                self.alive = False

    def __str__(self):
        return 'Name: {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}'.format(self)


# Troll subclass
class Troll(Enemy):
    """Subclass for Troll"""

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print('Me {0.name}. {0.name} stomp you!'.format(self))


# Vampire subclass
class Vampire(Enemy):
    """Subclass for Vampires"""

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=18)

    def take_damage(self, damage):  # Overriding superclass method
        if not self.dodges():
            super().take_damage(damage=damage)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print('***** {0.name} dodges *****'.format(self))
            return True
        else:
            return False


# Vampire King class
class VampireKing(Vampire):
    """Subclass for VampireKing"""

    def __init__(self, name):
        super().__init__(name)
        self.hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)
