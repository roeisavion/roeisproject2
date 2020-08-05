class Card():
    def __init__(self,value,suit):
        if 0<=value<=12:
            self.value=value
        else: self.value=0
        if 0<=suit<=3:
            self.suit=suit
        else: self.suit=0

    def __repr__(self):
        return f'{values[self.value]} {suits[self.suit]}'

    def __gt__(self, other):
        'define what is a bigger card'
        if self.value>other.value:
            return True
        if self.value==other.value:
            if self.suit>other.suit:
                return True
            else: return False
        else: return False

    def __eq__(self, other):
        if self.value==other.value and self.suit==other.suit :
            return True
        else: return False



values=['2','3','4','5','6','7','8','9','10','J','Q','k','A']
suits=['diamond','spade','heart','club']
