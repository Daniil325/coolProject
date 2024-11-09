import os
from typing import List

from core.card import Card


def get_image_cards() -> List[Card]:
    directory = "../assets/images"
    images = os.listdir(directory)
    list_images = []
    for image in images:
        rank, suit = image.split("_")
        if rank in ["King", "Queen", "Jack"]:
            rank = 10
        if rank == "Ace":
            rank = 11
        suit = suit.replace(".svg", "")
        # TODO: переделать, чтобы не создавался экземпляр класса для card_back
        if rank != "card":
            rank = int(rank)
            list_images.append(Card(rank, suit))
    return list_images

