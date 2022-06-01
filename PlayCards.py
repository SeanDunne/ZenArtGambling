from Cards import Deck
from random import choice

suits = ['spades', 'clubs', 'hearts', 'diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

class PlayCards():

    def __init__(self):
        self.pot_size = 0
        self.bet_size = 0
        self.draws = 0
        self.correct = 0
        self.incorrect = 0
        self.success_rate = 0

    def setup_deck(self):
        self.dealer_deck = Deck()
        self.cards_dealt = Deck()
        self.dealer_deck.fresh_deck(suits, ranks)
        self.dealer_deck.shuffle()

    def set_pot_size(self):
        self.pot_size = int(input('Please select your starting pot size: '))
        return self.pot_size

    def get_pot_size(self):
        return self.pot_size

    def set_bet_size(self, bet_style, whole):

        if (whole) and self.pot_size == 1:
            return 1

        if bet_style == 'quarter':
            bet_size = self.pot_size/4
        elif bet_style == 'half':
            bet_size = self.pot_size/2
        elif bet_style == 'max':
            bet_size = self.pot_size
        else:
            bet_size = input('Please select your bet amount: ')
            if int(float(bet_size)) > self.pot_size:
                print("Bet too large. Setting bet to max.")
                bet_size = self.pot_size

        if whole:
            return int(float(bet_size))
        else:
            return bet_size
        

    def colour_guess(self, colour_selector, auto_fin):

        colours = self.dealer_deck.count_colours()

        if (auto_fin) and (0 in colours):
            self.bet_style = 'max'

        if colour_selector == 'random':
            return choice(('r', 'b'))
        elif colour_selector == 'smart':
            if colours[0] > colours[1]:
                return 'r'
            elif colours[1] > colours[0]:
                return 'b'
            else:
                return choice(['r', 'b'])
        else:
            colour = input("Please choose a card colour ('r' or 'b'): ")
            if colour not in ('r', 'b'):
                print("Invalid colour selection.")
                self.colour_guess(colour_selector, auto_fin)
            return colour

    def make_bet(self, colour, bet_size):

        drawn_card = self.dealer_deck.get_top_card()

        if colour == 'r':
            colour_str = 'red'
        else:
            colour_str = 'black'

        print("----------------Drawing a card----------------")
        print("You bet {} that the card will be {}".format(bet_size, colour_str))
        print("The card is: {}".format(drawn_card))
        
        self.cards_dealt.add_card(self.dealer_deck.remove_card())
        self.draws += 1

        if drawn_card.colour == colour:
            self.pot_size += bet_size
            print("Correct! You win {}.".format(bet_size))
            self.correct += 1

        else:
            self.pot_size -= bet_size
            print("Incorrect.. You lose {}.".format(bet_size))
            self.incorrect += 1

        self.success_rate = (self.correct/self.draws) * 100
        
    def play(self, colour_selector="smart", bet_style="half", auto_fin=True, slow=False, whole=True):

        self.setup_deck()
        self.bet_style = bet_style
        self.pot_size = self.set_pot_size()

        playing = True

        while playing:
            if len(self.dealer_deck) > 0 and (self.pot_size > 0):
                
                colour = self.colour_guess(colour_selector, auto_fin)
                bet_size = self.set_bet_size(self.bet_style, whole)
                
                self.make_bet(colour, bet_size)

            else:
                playing = False
                break

            if slow:
                print("Your bet success rate is: {}%".format(self.success_rate))

            print("Your current pot size is: {}.".format(self.pot_size))
            self.dealer_deck.show_colours()
            if slow:
                input("----------------------------------------------")
            else:
                print("----------------------------------------------")
        
        print("You finished with a pot size of: {}".format(self.pot_size))
        
if __name__ == '__main__':

    game = PlayCards()
    game.play()
