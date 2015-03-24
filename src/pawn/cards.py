# coding: utf-8

import itertools


class Card(object):
    """Represents a playing card with suit and rank.

    :param suit: the card suit, usually one of ♠♥♦♣.
    :param rank: the card rank, usually one of A[2-10]JQK.
    """
    def __init__(self, suit=None, rank=None):
        if not all([suit, rank]):
            raise ValueError('Card should have both suit and rank defined,'
                             ' got {suit!r} and {rank!r}.'.format(
                                 suit=suit, rank=rank))
        self.suit = suit
        self.rank = rank


class Deck(object):
    '''The French standard playing card deck.'''
    card_class = Card
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit, rank
                      in itertools.product(self.suits, self.ranks)]
