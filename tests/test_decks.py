import sys 
import os 
import random

# inserting parent directory
sys.path.insert(0, os.getcwd())

from card import Card
from deck import Deck 

def test_deck_cards_len():
    deck_length = 52
    deck = Deck()

    assert len(deck.cards) == deck_length, f'Incorrect deck length! Expected {deck_length}, Actual: {len(deck.cards)}'


def test_get_all_cards():
    deck_length = 52
    deck = Deck()
    all_cards = deck.get_all_cards()

    assert len(all_cards) == deck_length, f'Get all cards did not returned {deck_length} number of cards!'

def test_draw_card():
    deck_length = 52
    deck = Deck()
    card = deck.draw_card()

    assert len(deck.used_cards) == 1, f'Incorrect length of used cards after draw! Expected 1, Actual: {len(deck.used_cards)}'
    assert len(deck.unused_cards) == deck_length - 1, f'Incorrect length of unused cards after draw! Expected {deck_length - 1}, actual {len(deck.unused_cards)}'
    assert deck.used_cards[0] == card, f'Expected card to be {card}, Actual: {deck.used_cards[0]}' 
    assert (card in deck.unused_cards) == False,  f'Error - card is found in unused_cards list!'


def test_draw_cards():
    deck_length = 52
    number_of_cards = random.randint(1, deck_length)
    deck = Deck()
    crnt_cards = deck.draw_cards(number_of_cards)

    assert len(deck.used_cards) == number_of_cards, f'Incorrect number of used cards! Expected: {number_of_cards}, Actual: {len(deck.used_cards)}!' 
    assert len(crnt_cards) == number_of_cards, f'Incorrect number of drawn cards! Expected: {number_of_cards}, Actual: {len(crnt_cards)}!'
    assert len(deck.unused_cards) == (deck_length - number_of_cards), f'Incorrect number of unused cards! Expected: {deck_length - number_of_cards}, Actual: {len(deck.unused_cards)}!'

    for card in crnt_cards:
        assert card in deck.used_cards, f'Card is not in used cards!'
        assert card not in deck.unused_cards, f'Card is in unused cards!'


def test_draw_card_no_cards_left():
    deck_length = 52
    deck = Deck()
    all_cards = deck.draw_cards(deck_length)

    assert deck.draw_card() == None, f'Card is not None after all cards are drawn'
    assert deck.draw_card() == None, f'Card is not None after all cards are drawn - second attempt'