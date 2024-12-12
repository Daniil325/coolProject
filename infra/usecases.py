from dataclasses import dataclass

from core.deck import Deck
from core.player import Dealer


@dataclass
class StartCommand:
    desk: Deck

    def __call__(self):
        return self.desk.generate_order()


@dataclass
class TakeCommand:
    deck: Deck

    def __call__(self):
        return self.deck.get_card()


@dataclass
class DealerTakeCommand:
    dealer: Dealer

    def __call__(self, cmd: TakeCommand, player_score: int):
        res = []
        while self.dealer.count_score() < player_score and self.dealer.count_score() != -1:
            res.append(self.dealer.take_card(cmd()))
        return res
