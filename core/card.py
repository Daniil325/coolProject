class Card:

    def __init__(self, rank: int):
        self._rank = rank

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
