class Card:

    def __init__(self, rank: int, suit: str):
        self._rank = rank
        self.suit = suit

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value
