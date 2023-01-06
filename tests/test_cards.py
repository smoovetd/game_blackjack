import pytest 
import sys 
import os 

# inserting parent directory
sys.path.insert(0, os.getcwd())

from card import Card


def test_to_str_card():
    crnt_char = 'A'
    crnt_sign = 'spades'
    card =  Card(crnt_char, crnt_sign)

    assert str(card).rstrip() == ' ___\n|A  |\n| \u2660 |\n|__A|'

