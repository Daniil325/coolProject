from typing import List

from core.card import Card
from core.exceptions import DomainError


class Player:

    def __init__(self, cards: List[Card] | None = None):
        self._money = 1000
        self.cards = cards

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        if value < 0:
            raise DomainError('Money cannot be negative')
        self._money = value

    def bet(self, bet_amount: int):
        self.money -= bet_amount
        return self.money

    def count_card_values(self):
        values_sum = 0
        for card in self.cards:
            values_sum += card.rank
        print(values_sum)
        return values_sum
