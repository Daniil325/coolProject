import random
from typing import List

from core.card import Card


class Deck:

    def __init__(self, cards: List[Card]):
        self.cards = cards

    def generate_order(self) -> List[Card]:
        random.shuffle(self.cards)
        return self.cards

    def get_card(self) -> Card:
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
