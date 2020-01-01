class Card:
    def __init__(self, num, text):
        self.owner = 'DrawPile'
        self.num = num
        self.text = text.split('<')[0]
        self.descr = text.split('<')[1][:-1]

    def print(self, full=False):
        if full:
            print(f'Card: num: {self.num:02}, owner: {self.owner}, text: {self.text}, descr: {self.descr}')
        else:
            print(f'Card: num: {self.num:02}, owner: {self.owner}, text: {self.text}')
