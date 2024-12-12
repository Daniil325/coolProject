from typing import List

from core.card import Card
from core.exceptions import DomainError


class BasePlayer:

    def __init__(self, cards: List[Card]):
        self.cards = [] if cards is None else cards

    def count_score(self):
        values_sum = 0
        for card in self.cards:
            values_sum += card.rank
        if values_sum > 21:
            return -1
        return values_sum

    def take_card(self, card: Card):
        self.cards.append(card)


class Player(BasePlayer):

    def __init__(self, cards: List[Card], money=1000):
        super().__init__(cards)
        self._money = money
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


class Dealer(BasePlayer):

    def __init__(self, cards: List[Card] | None = None):
        super().__init__(cards)
