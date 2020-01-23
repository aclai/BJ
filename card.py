class Card:
    #done
    def __init__ (self, suit, card_num, card_point, card_eng_name):
        self.suit = suit
        self.card_num = card_num
        self.card_point = card_point
        self.card_eng_name = card_eng_name
            
    #def return_suit(self, suit):
    #    return suit
    #    
    #def return_card_num(self):
     #   return self.card_num
    
    #def card_reader(self, suit, card_num):
    #    eng_suit = ["Diamond", "Club", "Heart", "Spade"]
    #    eng_num = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
    #    print (card_num)
    #    print (suit)
    #    print (eng_num[card_num])
    #    print (eng_suit[suit])
    #    print (str(eng_num[card_num]) + " of " + eng_suit[suit])   
    #    x = (str(eng_num[card_num]) + " of " + eng_suit[suit])
    #    return x