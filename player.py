from card import Card

class Player:
    '''Main class for player. Could be either person ro computer'''

    def __init__(self, player_type, name):
        self.name = name
        self.player_type = player_type
        self.cards = []

    def print_name(self):
        print(self.name)

    def print_player_type(self):
        print(self.player_type)

    def add_card(card: Card):
        if type(card) != Card:
            print('ERROR card has incorrect type!')
        else:
            self.cards.append(card)

    def clear_cards():
        self.cards = []
