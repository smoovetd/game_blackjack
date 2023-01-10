import sys 
import os 

# inserting parent directory
sys.path.insert(0, os.getcwd())

from card import Card
from deck import Deck 

def test_deck_cards_len():
    deck_length = 52
    deck = Deck()

    assert len(deck.cards) == deck_length, f'Incorrect deck length! Expected {deck_length}, Actual: {len(deck.cards)}'


def test_draw_card():
    deck_length = 52
    deck = Deck()
    card = deck.draw_card()

    assert len(deck.used_cards) == 1, f'Incorrect length of used cards after draw! Expected 1, Actual: {len(deck.used_cards)}'
    assert len(deck.unused_cards) == deck_length - 1, f'Incorrect length of unused cards after draw! Expected {deck_length - 1}, actual {len(deck.unused_cards)}'
    assert deck.used_cards[0] == card, f'Expected card to be {card}, Actual: {deck.used_cards[0]}' 
    assert (card in deck.unused_cards) == False,  f'Error - card is found in unused_cards list!'