import user
#Card Ranking:
#Blackjack (Ace + 10 points card without spliting)
#21 points --> 4 points

#check player no split
#translate hand into bj, or points for player
#translate hand into bj, or points for dealer

#


#else add up points Ace = 1 or 11

def calculate_hand(owner, hand):
    if len(hand) == 2 and 1 in hand and 10 in hand or 11 in hand or 12 in hand or 13 in hand:
        hand_value = 22
    else:
        hand_value = hand[1].card_num + hand[2].card_num
    if 1 in hand and points <= 11:
        hand_value = hand_value + 10        
    owner.hand_value(hand_value)
        
def compare_hand():
    if player.hand_value == dealer.hand_point:
        player.acct_balance = player.acct_balance + player.bet
    elif player.hand_value == 22:
        player.acct_balance = player.acct_balance + player.bet*2.5
    elif player.hand_value >= dealer.hand_value:
        player.acct_balance = player.acct_balance + player.bet*2
        
def new_game():
    deck.clear()
    dealerhand.clear()
    playerhand.clear()
    
def player_turn():

def dealer_turn():
    