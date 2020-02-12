"""
Subclass of Person
"""
import person

class Player(person.Person):
    def __init__(self):
        self.name = ""
        self.acct_balance = 0
        self.bet = 0
        self.hand = []
        self.hand_value = []
    
    def input_name(self):
        """
        This method allows players to choose a name
        """
        # takes any input for name
        self.name = input("Please enter your name:")

    def input_bet(self):
        """
        This method asks player to input a bet amount for each round
        """
        # infinite loop until player input accepted format and amount
        while True:
            try:
                bet_amount = int(input ("please enter your bet in millions of dollars: [1 - 100 million dollars]"))
            # if player input non-integer, ask again
            except ValueError:
                print("integer please")
                continue
            # if player input integer but outside of the allowed range, ask again
            if bet_amount <= 0 or bet_amount > 100:
                print("table limit is $1 - 100 million dollars")
                continue
            # if player wants to bet more than bankroll
            elif bet_amount > self.acct_balance:
                print("insufficinet funds")
                # ask to buy in more chips
                self.input_chip()
                continue
            # exit loop if input is accepted
            else:
                break    
        # deduct amount from bankroll
        self.bet = bet_amount
        bet_amount = bet_amount*(-1)
        self.adjust_fund(bet_amount)    
        print("your bankroll is now " + str(self.acct_balance))
    
    def input_chip(self):
        """
        This method asks player to buy in more chips
        """
        # infinite loop until palyer input acceted format and amount
        while True:
            try:
                input_chip = int(input ("please enter the number of chips in millions of dollars you would like to buy:"))
            # if player input non-interger, ask again
            except ValueError:
                print("integer please")
                continue
            # if player input interger but outside of allowed range, ask again
            if input_chip < 1000:
                print("the minimum you can buy is 1 billion / 1000 1-million-dollar chips")
                continue
            # if input is accepted, add amount to bankroll and exit loop
            else:
                self.adjust_fund(input_chip)
                break
    
    def adjust_fund(self, amount_to_adjust):
        """
        This method adjusts fund to the bankroll, both adding and subtracting, depending on amount_to_adjust
        """
        self.acct_balance = self.acct_balance + amount_to_adjust
        
    def add_hand_value(self, hand_value):
        """
        This method adds the input hand_value to player's .hand
        """
        self.hand_value.append(hand_value)
        
    
            
    
    
    #later when branch off blackjack and become universal & save user
    #def change_version(self, version_num):
    #def add_attribute(self, attribute_name):
    #def disable_attribute(self, attribute_name):
    #def enable_attribute(self, attribute_name):
    #def change_name(self, new_name):
    #def change_password(self, new_password):
    
    
    
        

    
    

