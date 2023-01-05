class Card:
    def __init__(self, char: str, sign: str) -> None:
        #self.char = char 
        #self.sign = sign
        self.set_char(char) 
        self.set_sign(sign)

    def set_char(self, char: str) -> None:
        valid_chars = ['A', 'K', 'Q' ,'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        if not char in valid_chars:
            print(f'ERROR: incorrect character: {char}. Valid values: {valid_chars}')        
            self.char = 'ERROR_CHAR'
        else:
            self.char = char

    def get_char(self) -> str:
        return self.char

    def set_sign(self, sign) -> None:
        valid_signs = {'spades': '\u2660', 'hearts': '\u2665', 'diamonds': '\u2666', 'cups': '\u2663'}
        if not sign in valid_signs.keys():
            print(f'ERROR: incorrect sign: {sign}. Expected signs are: {valid_signs.keys()}')
            self.sign = 'ERROR_SIGN'
        else:

            self.sign = valid_signs[sign]

    def get_sign(self):
        return self.sign

    def __str__(self) -> str:
        print(f'DEBUG INFO: char: {self.char} sign: {self.sign}')
        if self.char == '10':
            draw_card = f' ___\n|{self.get_char()} |\n| {self.get_sign()} |\n|_{self.get_char()}|\n'
        else: 
            draw_card = f' ___\n|{self.get_char()}  |\n| {self.get_sign()} |\n|__{self.get_char()}|\n'

        return draw_card

