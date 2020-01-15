import user
#Card Ranking:
#Blackjack (Ace + 10 points card without spliting)
#21 points --> 4 points
#else add up points Ace = 1 or 11

def calculate_hand(owner, hand):
    if len(hand) == 2 and 1 in hand and 10 or 11 or 12 or 13 in hand:
        hand_value = "bj"
    else:
        hand_value = 0
        for i in len(hand) + 1:
            hand_value = hand_value + hand[1].card_num
    if 1 in hand and points <= 11:
        hand_value = hand_value + 10        
        
def compare_hand():
    if player.hand_value == dealer.hand_point:
        player.acct_balance = player.acct_balance + player.bet
    elif player.hand_value == "bj":
        player.acct_balance = player.acct_balance + player.bet*2.5
    elif player.hand_value > dealer.hand_value:
        player.acct_balance = player.acct_balance + player.bet*2
    else:
        pass
        
def new_game():
    deck.clear()
    dealerhand.clear()
    playerhand.clear()
    #ask player if they want to a new game
        
def player_turn(player):
    hand_value = calculate_hand(player, hand)
    if len(player.hand) == 2:
        #check bj
        if hand_value == "bj":
            pass
        #check split        
        elif player.hand[0] == player.hand[1]:
            split_decision()
        #check double
        elif hand_value == 19 or 20 and 1 in hand and hand_value == 19 or 20 or hand_value == 9 or 10:
            double_decision():
        else:
            hit_decision()
    else:
        hit_decision()
    
def hit_decision():
    user-choice = input("do you want an additional card?[Y/N]")
        if user_choice == "Y" or "Yes" or "yes":
            deck.deal_card(player.hand)
            hand_value = calculate_hand(player, hand)
            if hand_value < 21:
                hit_decision()
            else:
                pass               
        elif user_choice == "N" or "No" or "no":
            pass
        else:
            print("please answer [Y/N]")
            hit_decision()

def split_decision():
    user-choice = input("do you want to split?[Y/N]")
        if user_choice == "Y" or "Yes" or "yes":
            removed_card = player.deck[0].remove_card(player)
            player.deck[1].add_card(removed_card)
            for i in num_of_hands:
                deck.deal_card(player.hand[i-1]
                player_turn(player.hand[i-1]
        elif user_choice == "N" or "No" or "no":
            hit_decision()
        else:
            print("please answer [Y/N]")
            split_decision()

def double_decision():
    user-choice = input("do you want to double down?[Y/N]")
        if user_choice == "Y" or "Yes" or "yes":
            player.acct_balance = player.acct_balance - player.bet
            player.bet = player.bet * 2
            deck.deal_card(player.hand)
        elif user_choice == "N" or "No" or "no":
            hit_decision()
        else:
            print("please answer [Y/N]")
            double_decision()            
           
def dealer_turn():
    