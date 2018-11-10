# Player Class
class Player(object):
    """Simple class to create new players"""

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _get_level(self):
        return self._level

    def _get_score(self):
        return self._score

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('Lives cannot be negative')
            self._lives = 0

    def _set_level(self, level):
        new_level = self._level + level
        if new_level >= 1:
            self._level = new_level
        else:
            self._level = 1

        self._score = (self._level - 1) * 1000

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)
    score = property(_get_score)

    # This will be called when the 'print' method is passed an instance of this class
    def __str__(self):
        return 'Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}'.format(self)
