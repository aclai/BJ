class Card:
    def __init__ (self, suit, card_num):
        self.suit = suit
        self.card_num = card_num
            
    def return_suit(self, suit):
        return suit
        
    def return_card_num(self, card_num):
        return card_num
    
    def card_reader(suit, card_num):
        eng_suit = ["Diamond", "Club", "Heart", "Spade"]
        eng_num = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
        print (card_num)
        print (suit)
        print (eng_num[card_num])
        print (eng_suit[suit])
        print (str(eng_num[card_num]) + " of " + eng_suit[suit])   