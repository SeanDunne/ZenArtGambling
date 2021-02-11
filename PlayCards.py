from Cards import Card, Deck

suits = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

class PlayCards():

    def __init__(self):
        self.pot_size = 0
        self.bet_size = 0
        self.setup_deck()

    def setup_deck(self):
        self.dealer_deck = Deck()
        self.cards_dealt = Deck()
        self.dealer_deck.fresh_deck(suits, ranks)
        self.dealer_deck.shuffle()

    def set_pot_size(self):
        return int(input('Please select your starting pot size: '))

    def get_pot_size(self):
        return self.pot_size

    def make_bet(self, bet_size):
        self.bet_size = self.set_bet_size()
        bet = input("Please choose a card colour ('r' or 'b'): ")
        draw = self.dealer_deck.get_top_card()
        if draw.color == bet:
            self.pot_size += self.bet_size
        else:
            self.pot_size -= self.bet_size
        
        self.cards_dealt.add_card(draw)

        print(self.pot_size)
        

    def set_bet_size(self):
        return int(input('Please select your bet amount: '))

    def play(self):

        self.pot_size = self.set_pot_size()

        playing = True

        while playing:
            if len(self.dealer_deck) > 0 and (self.pot_size > 0):
                self.make_bet(self.bet_size)
            
            else:
                playing = False

            self.cards_dealt.show_cards()

    
if __name__ == '__main__':
    game = PlayCards()
    '''print(game.dealer_deck.show_deck())'''
    '''print(len(game.dealer_deck))'''
    game.play()
