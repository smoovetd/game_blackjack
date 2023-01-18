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



def run(player1: Player, player2: Player):
    print(f'Added player: {player1}')
    print(f'Added player: {player2}')



if __name__ == '__main__':
    player1 = init_player('Player 1')
    player2 = init_player('Player 2')
    run(player1, player2)