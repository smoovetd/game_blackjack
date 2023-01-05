from typing import final
from card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.cards = self.get_full_deck()

        self.used_cards = list()

    def get_all_cards(self) -> tuple:
        return self.cards

    def draw_card(self) -> Card: 
        crnt_card = None
        while True:
            crnt_card = random.choice(self.cards)

            # if current card is already used, then another random card should be selected
            if not crnt_card in self.used_cards:
                self.used_cards.append(crnt_card)
                break

        return crnt_card


    def get_full_deck(self) -> tuple:
        all_cards =  (Card ('A', 'spades'), Card ('2', 'spades'), Card ('3', 'spades'), Card ('4', 'spades'), \
        Card ('5', 'spades'), Card ('6', 'spades'), Card ('7', 'spades'), Card ('8', 'spades'), \
        Card ('9', 'spades'), Card ('10', 'spades'), Card ('J', 'spades'), Card ('Q', 'spades'), \
        Card ('K', 'spades'), Card ('A', 'hearts'), Card ('2', 'hearts'), Card ('3', 'hearts'), \
        Card ('4', 'hearts'), Card ('5', 'hearts'), Card ('6', 'hearts'), Card ('7', 'hearts'), \
        Card ('8', 'hearts'), Card ('9', 'hearts'), Card ('10', 'hearts'), Card ('J', 'hearts'), \
        Card ('Q', 'hearts'), Card ('K', 'hearts'), Card ('A', 'diamonds'), Card ('2', 'diamonds'), \
        Card ('3', 'diamonds'), Card ('4', 'diamonds'), Card ('5', 'diamonds'), Card ('6', 'diamonds'), \
        Card ('7', 'diamonds'), Card ('8', 'diamonds'), Card ('9', 'diamonds'), Card ('10', 'diamonds'), \
        Card ('J', 'diamonds'), Card ('Q', 'diamonds'), Card ('K', 'diamonds'), Card ('A', 'cups'), \
        Card ('2', 'cups'), Card ('3', 'cups'), Card ('4', 'cups'), Card ('5', 'cups'), \
        Card ('6', 'cups'), Card ('7', 'cups'), Card ('8', 'cups'), Card ('9', 'cups'), \
        Card ('10', 'cups'), Card ('J', 'cups'), Card ('Q', 'cups'), Card ('K', 'cups'))

        return all_cards

    def print_all_cards(self) -> None:
        all_cards = ''
        for card in self.cards:
            all_cards += str(card) + '\n'

        print(all_cards)

    def print_list_cards(self, cards: list, cards_per_row:int = 4) -> None:
        cards_to_print = ''
        crnt_count = 0
        for card in cards:
            cards_to_print += str(card)

        crnt_cards = cards_to_print.split('\n')
        #print(crnt_cards)
        cards_list = list()
        final_str = ''
        count = 0
        for card_part in range (0,4):
            for card in range(card_part, len(crnt_cards) -1, 4):
                #print(f'part: {card_part}; card: {card}; current part of card: {crnt_cards[card]}')

                if card_part == 0 and card !=0:
                    final_str += ' '
                final_str += ' '

                final_str += crnt_cards[card]
                
            #print(f'DEBUG: {final_str}')   
            final_str = final_str + '\n'
            
            
        print(final_str)


deck = Deck()
#deck.print_all_cards()
cards_to_return = list()
cards_to_return.append(deck.get_all_cards()[0])
cards_to_return.append(deck.get_all_cards()[1])
cards_to_return.append(deck.get_all_cards()[2])
cards_to_return.append(deck.get_all_cards()[10])
#deck.print_list_cards(cards_to_return)
print(deck.draw_card())
print(deck.draw_card())
print(deck.draw_card())