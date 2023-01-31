import sys 
import os 

# inserting parent directory
sys.path.insert(0, os.getcwd())

from card import Card


def test_to_str_card():
    crnt_char = 'A'
    crnt_sign = 'spades'
    card =  Card(crnt_char, crnt_sign)

    assert str(card).rstrip() == ' ___\n|A  |\n| \u2660 |\n|__A|', 'Incorrect str()'


def test_eq_card_positive():
    card_first = Card('2', 'cups')
    card_second = Card('2', 'cups')

    assert card_first == card_second, f'Error in equal!'


def test_eq_card_negative():
    card_first = Card('2', 'cups')
    card_second = Card('2', 'spades')
    card_third = Card('3', 'cups')

    assert card_first != card_second, f'Error in equal - 2 cups equals 2 spades!'
    assert card_first != card_third, f'Error in equal - 2 cups equals 3 cups!'


def test_get_sign():
    card = Card('2', 'spades')
    assert card.get_sign() == '\u2660', f'Error in get_sign. Expected \u2660, Actual: {card.get_sign()}'


def test_get_char():
    card = Card('2', 'spades')
    assert card.get_char() == '2', f'Error in get_char. Expected 2, Actual: {card.get_char()}'