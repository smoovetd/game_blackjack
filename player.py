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

    def add_card(self, card: Card):
        if type(card) != Card:
            print('ERROR card has incorrect type!')
        else:
            self.cards.append(card)

    def clear_cards(self):
        self.cards = []

    def get_cards(self):
        return self.cards

    def __str__(self):
        return(f'Type: {self.player_type}; name: {self.name}, cards: {self.get_cards()}')

class Computer(Player):
    def __init__(self):
        name = 'Computer'
        player_type = 'computer'
        super().__init__(player_type, name)


class Person(Player):
    def __init__(self, name):
        name = name
        player_type = 'person'
        super().__init__(player_type, name)


pc = Computer()
pl = Person('Me')

pc.print_name()
pc.print_player_type()

pl.print_name()
pl.print_player_type()
