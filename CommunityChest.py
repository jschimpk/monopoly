from Card import Card
import random

cc_card_text = ['Advance to "Go". (Collect $200) <Mr. Monopoly goes to Go>',
                'Bank error in your favor. Collect $200. <Mr. Monopoly falls back in astonishment as an arm presents a sheaf of cash out of a bank teller\'s window>',
                'Doctor\'s fee. Pay $50. <Mr. Monopoly angrily brandishes crutches as he stomps with a leg cast>',
                'From sale of stock you get $50. <Mr. Monopoly, happily entangled in the tape of a stock ticker, waves cash (with no $ sign this time)>',
                'Get Out of Jail Free. This card may be kept until needed or sold/traded. <A winged Mr. M flutters out of a bird cage>',
                'Go to Jail. Go directly to jail. Do not pass Go, Do not collect $200. <A truncheon-wielding policeman in a light-colored uniform lifts a surprised Mr Monopoly by the collar>',
                'Grand Opera Night Opening. Collect $50 from every player for opening night seats. <A wall sign near steps reads "Opera Tonite - 8 PM Sharp"; Mr. Monopoly leans against it checking his pocket watch in annoyance>',
                'Holiday Fund matures. Collect $100. <Mr. Monopoly carries along a giant Xmas sock containing a sheaf of cash>',
                'Income tax refund. Collect $20. <Mr Monopoly faints back against a man displaying the Refund paper>',
                'It\'s your birthday. Collect $10 from every player. <Mr. Monopoly holds his gift and gets a M sign on the top of it.>',
                'Life insurance matures – Collect $100 <Below an I N S sign stands a bent Mr Monopoly, his long beard brushing the floor>',
                'Hospital Fees. Pay $100. <A bored nurse holds out her hand for payment while Mr. Monopoly holds 2 swaddled infants, one in each arm>',
                'School fees. Pay $50. <A bespectacled schoolboy unhappily receives a head pat and a dime ((Rockefeller style) from Mr. Monopoly.>',
                'Receive $25 consultancy fee. <As Justice of the Peace, a stern Mr. M holds out his hand for fee from an embarrassed groom whose bride hold a bouquet behind him>',
                'You are assessed for street repairs: Pay $40 per house and $115 per hotel you own. <Mr. Monopoly, supported by his near-ubiquitous cane in his left hand, holds a pick and shovel over his right shoulder>',
                'You have won second prize in a beauty contest. Collect $10. <Mr. Monopoly preens with a sash and large bouquet>',
                'You inherit $100. <Mr Monopoly. holds his head as unseen people\'s hands offer brochures titled "Buy Yacht", "World Tour", and "Rolls Royce">']


class CommunityChest(Card):
    pass


def create():
    return [CommunityChest(i, cc_card_text[i]) for i in range(len(cc_card_text))]


def unit_test():
    print('Printing all card texts:')
    for card in cc_card_text:
        print(f'{card}')
    deck = create()
    print('Created a deck. Print out all cards')
    for card in deck:
        print(f'Card: num: {card.num}, owner: {card.owner}, text: {card.text}')

    random.shuffle(deck)
    print('Shuffled deck. Here are the cards now:')
    for card in deck:
        print(f'Card: num: {card.num}, owner: {card.owner}, text: {card.text}')


if __name__ == '__main__':
    unit_test()
