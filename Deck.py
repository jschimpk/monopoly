import CommunityChest
import Chance
import random
import sys

g_cc_deck = None
g_ch_deck = None

class Deck:
    def __init__(self, type='CC', input=None):
        if type == 'CC':
            self.cards = CommunityChest.create()
            self.name = 'Community Chest'
        elif type == 'Chance':
            self.cards = Chance.create()
            self.name = 'Chance'
        else:
            print(f'Unknown deck type: {type}')
            raise NameError
        self.len = len(self.cards)
        self.draw_pile = self.cards.copy()
        self.discard_pile = []
        for card in self.cards:
            if 'Get Out of Jail Free' in card.text:
                self.jail_card = card

    def shuffle(self, pile='Discard'):
        if pile == 'Discard':
            source = self.discard_pile
            for card in source:
                card.owner = 'DrawPile'
        elif pile == 'Draw':
            source = self.draw_pile
        elif pile == 'Both':
            source = self.discard_pile + self.draw_pile
        elif pile == 'All':
            self.play_jail_card(do_print=False)
            source = self.discard_pile + self.draw_pile
        else:
            print(f'Unknown pile: {pile}')
            raise Exception
        random.shuffle(source)

        if pile == 'Discard':
            self.draw_pile += source
            self.discard_pile = []
        elif pile == 'Draw':
            self.draw_pile = source
        elif pile == 'Both':
            self.draw_pile = source
            self.discard_pile = []
        elif pile == 'All':
            self.draw_pile = source
            self.discard_pile = []

    def draw(self, player='Player', do_print=True):
        if len(self.draw_pile) == 0:
            if do_print == True:
                print(f'Draw {self.name} attempted, but draw pile is empty. Please shuffle and try again.')
                return
        card = self.draw_pile.pop(0)
        if do_print == True:
            total_text_len = len(card.text) + 12
            total_header_len = len(self.name) + 11
            spaces = ' '*(total_text_len // 2 - total_header_len // 2)
            print(f'{spaces}Draw {self.name} card.')
            bar = '*'* total_text_len
            print(bar)
            print(f'****  {card.text}  ****')
            print(bar)
            print(f'< {card.descr} >')

        if card == self.jail_card:
            card.owner = player
        else:
            card.owner = 'DiscardPile'
            self.discard_pile.append(card)
        return card


    def play_jail_card(self, do_print=True):
        if 'Player' in self.jail_card.owner:
            if do_print:
                print(f'Get Out of Jail Free card played. Returning to {self.name} Discard Pile...')
            self.jail_card.owner = 'DiscardPile'
            self.discard_pile.append(self.jail_card)
            return True
        else:
            if do_print:
                print(f'Error! "Get Out of Jail Free" {self .name} card not owned by Player. Try again...')
            return False


    def print(self):
        for card in self.cards:
            card.debug_print()

    def print_piles(self):
        print('Draw Pile')
        for card in self.draw_pile:
            card.debug_print()
        print('Discard Pile')
        for card in self.discard_pile:
            card.debug_print()
        if self.jail_card.owner == 'Player':
            print('Player')
            self.jail_card.debug_print()

    def print_stats(self):
        print(f'{self.name} cards are distributed as follows:')
        print(f'Draw Pile: {len(self.draw_pile)}')
        print(f'Discard Pile: {len(self.discard_pile)}')
        print(f'Player Pile:  {1 if self.jail_card.owner == "Player" else 0}')


def unit_test():
    for deck_name in ['CC', 'Chance']:
        print(f'Deck: {deck_name}')
        my_deck = Deck(deck_name)
        print(f'Starting Unit tests for Deck: {my_deck.name}')
        print(f'Printing unshuffled cards:')
        for card in my_deck.draw_pile:
            card.debug_print()
        # Draw all the cards
        for i in range(len(my_deck.draw_pile)):
            card = my_deck.draw(do_print=False)
            card_str = card.debug_print(return_str=True)
            print(f'Unit test draw: {i}. Got card: {card_str}')
            if card.num is not i:
                print(f'Cards out of sequence! i: {i}  card.num: {card.num}')
        # Draw from empty pile
        card = my_deck.draw()
        if card:
            print('Drew extra card:')
            card.debug_print()
        else:
            print('Empty draw pile test succeeded.')

        #Shuffle cards
        my_deck.shuffle(pile='All')
        print(f'Shuffle cards and print:')
        for card in my_deck.draw_pile:
            card.debug_print()

'''
        card = my_deck.draw()
        print('Drew card:')
        card.print()
        print('CC Deck:')
        my_deck.print()
        my_deck.print_stats()
        my_deck.print_piles()
        my_deck.shuffle()
        print('Shuffle CC Deck')
        print('CC Deck:')
        my_deck.print()
        my_deck.print_stats()
        my_deck.print_piles()
'''

if __name__ == '__main__':
    unit_test()
