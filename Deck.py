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


    def draw(self, player=None, do_print=True):
        if len(self.draw_pile) == 0:
            if do_print == True:
                print(f'Draw {self.name} attempted, but draw pile is empty. Please shuffle and try again.')
                return
        #card = self.draw_pile.pop(random.randrange(len(self.draw_pile)))
        card = self.draw_pile.pop(0)
        if do_print == True:
            print(f'Draw {self.name} card. You got: {card.text}')
        if card == self.jail_card:
            if player is not None:
                card.owner = player
        else:
            if player == 'Shuffle':
                card.owner = 'DrawPile'
            else:
                card.owner = 'DiscardPile'
                self.discard_pile.append(card)
        return card


    def print(self):
        for card in self.cards:
            card.print()

    def print_piles(self):
        print('Draw Pile')
        for card in self.draw_pile:
            card.print()
        print('Discard Pile')
        for card in self.discard_pile:
            card.print()
        if self.jail_card.owner == 'Player':
            print('Player')
            self.jail_card.print()

    def print_stats(self):
        print(f'{self.name} cards are distributed as follows:')
        print(f'Draw Pile: {len(self.draw_pile)}')
        print(f'Discard Pile: {len(self.discard_pile)}')
        print(f'Player Pile:  {1 if self.jail_card.owner == "Player" else 0}')

def unit_test():
    cc_deck = Deck('CC')
    chance_deck = Deck('Chance')

    print('CC Deck:')
    cc_deck.print()
    card = cc_deck.draw()
    print('Drew card:')
    card.print()
    print('CC Deck:')
    cc_deck.print()
    cc_deck.print_piles()
    cc_deck.shuffle()
    print('Shuffle CC Deck')
    print('CC Deck:')
    cc_deck.print()
    cc_deck.print_piles()


def print_jail_menu():
    print('Play Get Out of Jail Free Card. Choose which card:')
    print('1. Community Chest')
    print('2. Chance')
    print('3. Go Back...')

def run_jail_menu():
    global g_cc_deck
    global g_ch_deck

    selection_is_valid = False
    while selection_is_valid == False:
        print_jail_menu()
        selection_is_valid = True
        try:
            selection = input('Enter choice: ')
        except KeyboardInterrupt:
            print('\n\n<CTRL-C> detected. Exit...')
            sys.exit()
        except Exception as e:
            print(f'Received Exception: {str(e)}')
            raise e

        if selection == '1':
            source = g_cc_deck
        elif selection == '2':
            source = g_ch_deck
        elif selection == '3':
            return
        else:
            selection_is_valid = False
            print(f'Unknown selection: {selection}. Try again...')
            continue

        if 'Player' in source.jail_card.owner:
            print(f'Get Out of Jail Free card played. Returning to {source.name} Discard Pile...')
            source.jail_card.owner = 'DiscardPile'
            source.discard_pile.append(source.jail_card)
        else:
            print(f'Error! "Get Out of Jail Free" {source.name} card not owned by Player. Try again...')
            selection_is_valid = False


def print_shuffle_menu(deck):
    print(f'Shuffle {deck.name}. Choose source:')
    print('1. Both. Shuffle all cards and place in draw pile.')
    print('2. Discard pile. Shuffle and add to bottom of draw pile.')
    print('3. Draw pile.  Shuffle draw pile and leave discard as-is.')
    print('4. Go back...')

def shuffle_menu(deck):
    selection_is_valid = False
    while selection_is_valid == False:
        print_shuffle_menu(deck)
        selection_is_valid = True
        try:
            selection = input('Enter choice: ')
        except KeyboardInterrupt:
            print('\n\n<CTRL-C> detected. Exit...')
            sys.exit()
        except Exception as e:
            print(f'Received Exception: {str(e)}')
            raise e

        if selection == '1':
            pile = 'Both'
        elif selection == '2':
            pile = 'Discard'
        elif selection == '3':
            pile = 'Draw'
        elif selection == '4':
            return
        else:
            selection_is_valid = False
            print(f'Unknown selection: {selection}. Try again...')

    deck.shuffle(pile=pile)

def print_menu():
    print('Menu:')
    print('1. Draw Community Chest Card')
    print('2. Draw Chance Card')
    print('3. Play Get Out of Jail')
    print('4. Shuffle Community Chest')
    print('5. Shuffle Chance')
    print('6. Print Piles')
    print('7. Print Stats')


def run_menu():
    global g_cc_deck
    global g_ch_deck

    selection_is_valid = False
    while selection_is_valid == False:
        selection_is_valid = True
        print_menu()
        try:
            selection = input('Enter choice: ')
        except KeyboardInterrupt:
            print('\n\n<CTRL-C> detected. Exit...')
            sys.exit()
        except Exception as e:
            print(f'Received Exception: {str(e)}')
            raise e

        if selection == '1':
            card = g_cc_deck.draw(player='Player')
        elif selection == '2':
            card = g_ch_deck.draw(player='Player')
        elif selection == '3':
            run_jail_menu()
        elif selection == '4':
            shuffle_menu(g_cc_deck)
        elif selection == '5':
            shuffle_menu(g_ch_deck)
        elif selection == '6':
            print('Community chest:')
            g_cc_deck.print_piles()
            print('Chance:')
            g_ch_deck.print_piles()
        elif selection == '7':
            g_cc_deck.print_stats()
            g_ch_deck.print_stats()
        else:
            selection_is_valid = False
            print(f'Unknown selection: "{selection}".  Try again...')



def run_game():
    global g_cc_deck
    global g_ch_deck

    g_cc_deck = Deck('CC')
    g_ch_deck = Deck('Chance')
    g_cc_deck.shuffle(pile='Draw')
    g_ch_deck.shuffle(pile='Draw')

    while 1:
        run_menu()


if __name__ == '__main__':
    #unit_test()
    run_game()
