class Card:
    def __init__(self, num, text):
        self.owner = 'DrawPile'
        self.num = num
        self.text = text.split('<')[0]
        self.descr = text.split('<')[1][:-1]

    def print(self, return_str=False):
        if return_str:
            return [self.text, self.descr]
        print(self.text)
        print(self.descr)

    def debug_print(self, full=False, return_str=False):
        my_string = f'Card: num: {self.num:02}, owner: {self.owner}, text: {self.text}'
        if full:
            my_string += f', descr: {self.descr}'
        if return_str:
            return my_string
        print(my_string)
'''
        if full:
            print(f'Card: num: {self.num:02}, owner: {self.owner}, text: {self.text}, descr: {self.descr}')
        else:
            print(f'Card: num: {self.num:02}, owner: {self.owner}, text: {self.text}')
            '''
