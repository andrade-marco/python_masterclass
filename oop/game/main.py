from Player import Player
from Enemy import Troll, Vampire, VampireKing

tim = Player('Tim')

ugly_troll = Troll('Urg')
another_troll = Troll('Ug')
first_vampire = Vampire('Dracula')

print(ugly_troll)
print(another_troll)
print(first_vampire)

first_vampire.take_damage(10)
print(first_vampire)

vamp_king = VampireKing('KingDracula')
print(vamp_king)

while vamp_king.alive:
    vamp_king.take_damage(12)
    print(vamp_king)

print('*' * 40)
