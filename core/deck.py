import random
from typing import List

from core.card import Card


class Deck:

    def __init__(self, cards: List[Card]):
        self.cards = cards

    def generate_order(self):
        return random.shuffle(self.cards)

    def get_card(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
