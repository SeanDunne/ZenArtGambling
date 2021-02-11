from random import shuffle, choice

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.color = self.get_color()

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def get_color(self):
        if self.suit == 'diamonds' or self.suit == 'hearts':
            return 'r'
        if self.suit == 'spades' or self.suit == 'clubs':
            return 'b'

class Deck:
    def __init__(self):
        self.deck = []

    def __str__(self):
        return str([str(card) for card in self.deck])
    
    def __len__(self):
        return len(self.deck)
    
    def fresh_deck(self, suits, ranks):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranks]

    def show_cards(self):
        for card in self.deck:
            print(card)
    
    def len_deck(self):
        return(len(self.deck))

    def shuffle(self):
        shuffle(self.deck)
    
    def get_top_card(self):
        return self.deck[-1]

    def remove_card(self):
        if self.len_deck() > 0:
            return self.deck.pop(-1)

    def add_card(self, card):
        self.deck.append(card)
    
    def count_colors(self):
        r_count = 0
        b_count = 0
        for card in self.deck:
            if card.get_color() == 'r':
                r_count += 1
            if card.get_color() == 'b':
                b_count += 1
        
        return (r_count, b_count)
