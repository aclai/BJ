import deck

class User:
    #done
    def __init__(self, version=1, user_id=1):
        self.version = version
        self.user_id = user_id
        self.name = ""
        self.password = ""
        self.acct_balance = 0
        self.bet = 0
        self.hand = []
        self.hand_value = []
    
    #done
    def input_name(self):
        self.name = input("Please enter your name:")

    def input_bet(self):
        while True:
            try:
                bet_amount = int(input ("please enter your bet in millions of dollars:"))
            except ValueError:
                print("integer please")
                continue
            if bet_amount <= 0 or bet_amount > 100:
                print("table limit is $1 - 100 million dollars")
                continue
            elif bet_amount > acct_balance:
                print("insufficinet funds")
                add_fund
                continue
            else:
                break    
        self.bet = bet_amount
        bet_amount = bet_amount*(-1)
        add_fund(bet_amount)       
        
    def hand_value(self, value):
        self.hand_value.append(value)
    
    #done
    def input_chip(self):
        while True:
            try:
                input_chip = int(input ("please enter the number of chips in millions of dollars you would like to buy:"))
            except ValueError:
                print("integer please")
                continue
            if input_chip <= 1000:
                print("the minimum you can buy is 1 billion / 1000 1-million-dollar chips")
                continue
            else:
                self.acct_balance = self.acct_balance + input_chip
                break
            
    def create_empty_hands(self):
        for i in [1,2,3,4]:
            self.hand.append(deck.Deck("player_hand_" + str(i)))
            
    
    
    #later when branch off blackjack and become universal & save user
    #def change_version(self, version_num):
    #def add_attribute(self, attribute_name):
    #def disable_attribute(self, attribute_name):
    #def enable_attribute(self, attribute_name):
    #def change_name(self, new_name):
    #def change_password(self, new_password):
    
    
    
        

    
    

