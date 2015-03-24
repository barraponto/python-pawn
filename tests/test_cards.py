# coding: utf-8

import itertools

import pytest

from pawn.cards import Card, Deck


@pytest.mark.parametrize('suit,rank',
                         itertools.product(['♣', '♥'], ['A', '3']))
def test_card(suit, rank):
    card = Card(suit=suit, rank=rank)
    assert card.suit == suit
    assert card.rank == rank

@pytest.mark.parametrize('suit,rank',
                         [pytest.mark.xfail((None, None), raises=ValueError),
                          pytest.mark.xfail(('♣', None), raises=ValueError),
                          pytest.mark.xfail((None, '3'), raises=ValueError)])
def test_bad_card(suit, rank):
    assert Card(suit=suit, rank=rank)

def test_deck():
    deck = Deck()
    assert len(deck.cards) == 52

def test_deck_card_class():

    class TestCard(Card):
        pass

    class TestDeck(Deck):
        card_class = TestCard

    deck = TestDeck()
    assert type(deck.cards[0]) == TestCard

