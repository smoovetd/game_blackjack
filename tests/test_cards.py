import pytest 
import sys 
import os 

# inserting parent directory
print(os.getcwd())
sys.path.insert(0, os.getcwd())

from card import Card


@pytest.fixture(scope="class")
def test_to_str_card():
    card = Card('A', 'spades')
    assert str(card) == '___\n|A  |\n| \u2660 |\n|__A|aaa'

