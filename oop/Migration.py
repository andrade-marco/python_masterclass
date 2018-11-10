import Ducks

flock = Ducks.Flock()
duck1 = Ducks.Duck()
duck2 = Ducks.Duck()
duck3 = Ducks.Duck()
duck4 = Ducks.Duck()
duck5 = Ducks.Duck()
duck6 = Ducks.Duck()
duck7 = Ducks.Duck()
percy = Ducks.Penguin()

duck_list = [duck1, duck2, duck3, percy, duck4, duck5, duck6, duck7]
for duck in duck_list:
    flock.add_duck(duck)

flock.migrate()
