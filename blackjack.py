from player import Player, Computer, Person 
from card import Card 
from deck import Deck

def abort_the_game():
    print('Aborting the game,')
    quit() 

def init_player(player_name, max_fail_attempts=5):
    player_type = None
    count_attempt = 0

    while(player_type != 'computer' and player_type != 'person'):
        player_type = input(f'Enter player type: "computer" or "person" for {player_name}: ')
        count_attempt += 1
        player = None
        if (count_attempt >= max_fail_attempts):
            print(f'ERROR: You were not able to provide correct player time in {max_fail_attempts} times')
            abort_the_game()

    if player_type == 'person':
        name = input('Enter name for {player_name}: ')        
        player = Person(name)
    elif player_type == 'computer':
        player = Computer()
    else:
        print(f'ERROR -> incorrect player type was used: {player_type}')
        abort_the_game()

    return player


def get_cards_strength(card: Card, is_first=False):
    strength = 0

    if card.get_char().isnumeric() == True:
        strength = int(card.get_char())
    elif card.get_char() == 'A' and is_first == True:
        strength = 11
    elif card.get_char() == 'A' and is_first == False:
        strength = 1
    elif card.get_char() in ['K', 'Q', 'J']:
        strength = 10
    else:
        print(f'ERROR get_cards_strength() -> incorrect character returned: {card.get_char()}')
        strength = -1

    return strength
    

def get_players_card_stregth(cards: list):
    total_strength = 0
    is_first = True
    for card in cards:
        if not (card.__class__ == Card):
            print(f'ERROR: incorrect card type:  {type(card)}, expected {Card.__class__}')
            abort_the_game()
        
        total_strength += get_cards_strength(card, is_first= is_first)
        is_first = False 

    return total_strength


def start_game(player1: Player, player2: Player):
    print('Game is started!')
    deck = Deck()

    player1.add_card(deck.draw_card())
    player1.add_card(deck.draw_card())

    player2.add_card(deck.draw_card())
    player2.add_card(deck.draw_card())

    print('Player 1 hand: ')
    deck.print_list_cards(player1.cards)
    print(f'Player 1 strength: {get_players_card_stregth(player1.cards)}')

    print('Player 2 hand: ')
    deck.print_list_cards(player2.cards)
    print(f'Player 2 strength: {get_players_card_stregth(player2.cards)}')


def run(player1: Player, player2: Player):
    print(f'Added player: {player1}')
    print(f'Added player: {player2}')
    
    start_game(player1, player2)


if __name__ == '__main__':
    player1 = init_player('Player 1')
    player2 = init_player('Player 2')
    run(player1, player2)