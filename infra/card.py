import os
from typing import List

from core.card import Card


def get_image_cards() -> List[Card]:
    directory = "./assets/images"
    images = os.listdir(directory)
    list_images = []
    for image in images:
        rank, suit = image.split("_")

        if rank in ["King", "Queen", "Jack"]:
            suit = suit + f"_{rank}"
            rank = 10
        if rank == "Ace":
            suit = suit + f"_{rank}"
            rank = 11

        suit = suit.replace(".svg", "")
        # TODO: переделать, чтобы не создавался экземпляр класса для card_back
        if rank != "card":
            rank = int(rank)
            list_images.append(Card(rank, suit))
    return list_images


def get_card_file(rank: int, suit: str):
    s = suit
    r = rank
    if "_" in suit:
        suit, rank = suit.split("_")
    file = f"./assets/images/{rank}_{suit}.svg"
    return file
