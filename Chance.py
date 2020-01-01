from Card import Card
import random

chance_card_text = ['Advance to "Go". (Collect $200) <Mr. Monopoly hops on both feet.>',
                    'Advance to Illinois Ave. If you pass Go, collect $200. <Mr. Monopoly has tied a cloth bundle onto his cane to make a bindle, carried over his right shoulder, and is smoking a cigar>',
                    'Advance to St. Charles Place. If you pass Go, collect $200. <Mr. Monopoly hurries along, hauling a little boy by the hand>',
                    'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total 10 times the amount thrown. <Mr. Monopoly trudges along with a huge battleship token on his back>',
                    'Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank. <At lower left, Mr. Monopoly carries a large flatiron token with two hands; at upper right a railroad crossing is seen>',
                    'Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank. <At lower left, Mr. Monopoly carries a large flatiron token with two hands; at upper right a railroad crossing is seen>',
                    'Bank pays you dividend of $50. <With his feet up on a telephone-bearing desk, Mr. Monopoly leans back in an overstuffed chair, blowing cigar smoke rings>',
                    'Get Out of Jail Free. This card may be kept until needed, or traded/sold. <Mr. Monopoly, in close-fitting one-piece prison stripes, is literally kicked out>',
                    'Go Back Three Spaces. <Mr. Monopoly is hauled back by a cane hooked around his neck>',
                    'Go to Jail. Go directly to Jail. Do not pass GO, do not collect $200. <A truncheon-carrying policeman in a dark-colored uniform hauls a surprised Mr Monopoly along by the feet>',
                    'Make general repairs on all your property: For each house pay $25, For each hotel pay $100. <Consulting a "How to Fix It" brochure, a hammer-wielding Mr. Monopoly sits astride a house not much larger than he is; it buckles under his weight>',
                    'Pay poor tax of $15 <His trouser pockets pulled out to show them empty, Mr. Monopoly spreads his hands>',
                    'Take a ride to Reading. Advance token to Reading Railroad. If you pass Go, collect $200. <Mr. Monopoly rides astride the TOOTing engine of a train>',
                    'Take a walk on the Boardwalk. Advance token to Boardwalk. <Mr. Monopoly, a smallish dog hung over one arm, with the other pushes a squalling baby in a small pram; behind them, birds fly in the sky above a low fence>',
                    'You have been elected Chairman of the Board. Pay each player $50. <A newsboy shouts an Extra with Mr. Monopoly\'s headshot on its front page>',
                    'Your building loan matures. Collect $150. <Mr. Monopoly joyfully embraces an apparent wife>']

class Chance(Card):
    pass


def create():
    return [Chance(i, chance_card_text[i]) for i in range(len(chance_card_text))]


def unit_test():
    print('Printing all card texts:')
    for card in chance_card_text:
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

