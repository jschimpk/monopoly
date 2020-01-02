#import CommunityChest
#import Chance
import Deck

def print_jail_menu():
    print('Play Get Out of Jail Free Card. Choose which card:')
    print('1. Community Chest')
    print('2. Chance')
    print('3. Go Back...')


def jail_menu():
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
            my_deck = g_cc_deck
        elif selection == '2':
            my_deck  = g_ch_deck
        elif selection == '3':
            return
        else:
            selection_is_valid = False
            print(f'Unknown selection: {selection}. Try again...')
            continue

        if my_deck.play_jail_card():
            selection_is_valid = True


def print_shuffle_menu(deck):
    print(f'Shuffle {deck.name}. Choose source:')
    print('1. All Cards. Shuffle all cards and place in draw pile.')
    print('2. All Cards + Jail. Retrieve jail card if given out and shuffle all cards.')
    print('3. Just Discard pile. Shuffle and add to bottom of draw pile.')
    print('4. Just Draw pile.  Shuffle draw pile and leave discard as-is.')
    print('5. Go back...')

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
        if selection == '2':
            pile = 'All'
        elif selection == '3':
            pile = 'Discard'
        elif selection == '4':
            pile = 'Draw'
        elif selection == '5':
            return
        else:
            selection_is_valid = False
            print(f'Unknown selection: {selection}. Try again...')

    deck.shuffle(pile=pile)


def print_main_menu():
    print('Menu:')
    print('1. Draw Community Chest Card')
    print('2. Draw Chance Card')
    print('3. Play Get Out of Jail')
    print('4. Shuffle Community Chest')
    print('5. Shuffle Chance')
    print('6. Print Piles')
    print('7. Print Stats')


def run_main_menu():
    global g_cc_deck
    global g_ch_deck

    selection_is_valid = False
    while selection_is_valid == False:
        selection_is_valid = True
        print_main_menu()
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
            jail_menu()
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

    g_cc_deck = Deck.Deck('CC')
    g_ch_deck = Deck.Deck('Chance')
    g_cc_deck.shuffle(pile='Draw')
    g_ch_deck.shuffle(pile='Draw')

    while 1:
        run_main_menu()


if __name__ == '__main__':
    run_game()
