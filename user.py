import deck

class User:
    
    def __init__(self, name, acct_balance, version=1, user_id=None, password=1234):
        self.version = version
        self.user_id = user_id
        self.name = name
        self.password = password
        self.acct_balance = acct_balance
        self.bet = bet
        self.hand = []
        self.hand_value = []
        
    def create_user(self):
        name = input("Please enter User name")
        acct_balance = input_chip
        player = User(name, acct_balance)

    def bet(self):
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
        bet = bet_amount
        bet_amount = bet_amount*(-1)
        add_fund(bet_amount)       

    def add_fund(self):
        amount = input_chip
        acct_balance = acct_balance + amount
        
    def hand_value(self, value):
        hand_value.append(value)
    
    def input_chip(self):
        while True:
            try:
                acct_balance = int(input ("please enter the number of chips in millions of dollars you would like to buy"))
            except ValueError:
                print("integer please")
                continue
            if acct_balance <= 1000:
                print("the minimum you can buy is 1 billion / 1000 1-million-dollar chips")
                continue
            return acct_balance
    
    
    
    #later when branch off blackjack and become universal & save user
    #def change_version(self, version_num):
    #def add_attribute(self, attribute_name):
    #def disable_attribute(self, attribute_name):
    #def enable_attribute(self, attribute_name):
    #def change_name(self, new_name):
    #def change_password(self, new_password):
    
    
    
        

    
    
