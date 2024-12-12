from flet import Page, Container, Margin
import flet as ft

from core.deck import Deck
from core.player import Player, Dealer
from infra.card import get_image_cards, get_card_file
from infra.usecases import StartCommand, TakeCommand, DealerTakeCommand
from presentation.base import base_page, WIDTH, HEIGHT

cards = get_image_cards()
desk = Deck(cards)
take_card = TakeCommand(desk)
p_card1 = take_card()
p_card2 = take_card()
f1 = get_card_file(p_card1.rank, p_card1.suit)
f2 = get_card_file(p_card2.rank, p_card2.suit)
p = Player([p_card1, p_card2])


dealer = Dealer(cards)

img1 = ft.Image(
    src=f1,
    width=50,
    height=100,
    fit=ft.ImageFit.COVER,
    repeat=ft.ImageRepeat.NO_REPEAT,
    border_radius=ft.border_radius.all(10)
)

img2 = ft.Image(
    src=f2,
    width=50,
    height=100,
    fit=ft.ImageFit.COVER,
    repeat=ft.ImageRepeat.NO_REPEAT,
    border_radius=ft.border_radius.all(10)
)

images = ft.Row(expand=1, wrap=False, left=300, top=0, right=0, bottom=0)

d_images = ft.Row(expand=1, wrap=False, left=300, top=0, right=0, bottom=0)

score_field = ft.TextField(label="Ваш счет", read_only=True, width=100, bgcolor="white",
                           color="black", hint_style=ft.TextStyle(color="black"))

money_field = ft.TextField(label="Ваши деньги", read_only=True, value=p.money, width=100, bgcolor="white",
                           color="black", hint_style=ft.TextStyle(color="black"))

bet_field = ft.TextField(label="Ваша ставка:", value="50", width=100, bgcolor="white", color="black")


def reset():
    global cards, desk, take_card, p_card1, p_card2, f1, f2, img1, img2, p
    cards = get_image_cards()
    desk = Deck(cards)
    take_card = TakeCommand(desk)
    p_card1 = take_card()
    p_card2 = take_card()
    p = Player([p_card1, p_card2], int(money_field.value))
    f1 = get_card_file(p_card1.rank, p_card1.suit)
    f2 = get_card_file(p_card2.rank, p_card2.suit)

    img1 = ft.Image(
        src=f1,
        width=50,
        height=100,
        fit=ft.ImageFit.COVER,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10)
    )

    img2 = ft.Image(
        src=f2,
        width=50,
        height=100,
        fit=ft.ImageFit.COVER,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(10)
    )

    images.controls = []
    d_images.controls = []
    score_field.value = "0"



def dealer_container():
    st = ft.Stack([
        Container(
            width=WIDTH, height=HEIGHT / 3, margin=0, padding=0
        ),
        d_images,
    ])

    return st


def score_value_update(page):
    score_field.value = p.count_score()
    page.update()


def middle_container(page):
    blank_image = "./assets/images/card_back.png"
    img = ft.DecorationImage(blank_image)

    st = ft.Stack([
        Container(
            image=img,
            width=75,
            height=150,
        ),
    ])
    return st


def player_cards_container(page):
    margin = Margin(left=300, top=0, right=0, bottom=0)

    def deck_click(e):
        d = take_card()
        p.take_card(d)
        f = get_card_file(d.rank, d.suit)
        img = ft.Image(
            src=f,
            width=50,
            height=100,
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(10)
        )
        images.controls.append(img)
        score_field.value = str(p.count_score())
        if p.count_score() == -1:
            bet_sum = int(bet_field.value) * 2
            p.money -= bet_sum
            money_field.value = p.money
            score_field.value = "0"
            reset()
        if p.count_score() == 21:
            bet_sum = int(bet_field.value) * 2
            p.money += bet_sum
            money_field.value = p.money
            score_field.value = "0"
            reset()
        page.update()

    def bet_confirm(e):
        cmd = StartCommand(desk)
        images.controls.append(img1)
        images.controls.append(img2)
        money_field.value -= int(bet_field.value)

        d_card1 = take_card()
        d_card2 = take_card()
        dealer.take_card(d_card1)
        dealer.take_card(d_card2)
        score_field.value = p.count_score()
        p.take_card(d_card1)

        df1 = get_card_file(d_card1.rank, d_card1.suit)
        df2 = get_card_file(d_card2.rank, d_card2.suit)

        dimg1 = ft.Image(
            src=df1,
            width=50,
            height=100,
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(10)
        )

        dimg2 = ft.Image(
            src=df2,
            width=50,
            height=100,
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
            border_radius=ft.border_radius.all(10)
        )
        d_images.controls.append(dimg1)
        d_images.controls.append(dimg2)

        page.update()

    def take_yourself(e):
        dtc = DealerTakeCommand(dealer)
        a = dtc(take_card(), p.count_score())
        bet_sum = int(bet_field.value) * 2
        p.money += bet_sum
        money_field.value = p.money
        score_field.value = "0"
        reset()
        page.update()

    st = ft.Stack([
        Container(
            width=400, height=150, bgcolor="#4d3432", margin=margin,
            alignment=ft.alignment.center, border_radius=30,
        ),
        images,
        ft.Column(
            controls=[
                ft.Row(controls=[score_field, money_field]),
                ft.Row(controls=[
                    ft.FilledTonalButton(text="Взять карту", on_click=deck_click),
                    ft.FilledTonalButton(text="Себе", on_click=take_yourself),
                ]),
                ft.Row(controls=[
                    bet_field,
                    ft.FilledTonalButton(text="Подтвердить ставку", on_click=bet_confirm),
                ])
            ]
        )

    ])
    return st


def play_page(page: Page):
    c1 = dealer_container()
    c2 = middle_container(page)
    c3 = player_cards_container(page)
    base_page(page)
    page.add(c1)
    page.add(c2)
    page.add(c3)
