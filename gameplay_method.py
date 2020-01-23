def player_turn(player_hand, main_deck):
    player_hand.move_random_card(main_deck)
    print("second card player receive:")
    print(player_hand[1].card_eng_name)
    print("length of main_deck:")
    print(len(main_deck))
    hand_value = calculate_hand(player_hand)
    #check bj
    print(hand_value)
    if hand_value == "bj":
        pass
    elif len(player_hand) == 2:
        #check split        
    #    if player_hand[0].card_point == player_hand[1].card_point:
    #        split_decision(player_hand, main_deck)
        #check double
        if hand_value == 20 and 1 in player_hand or hand_value == 9 or hand_value == 10:
            double_decision(player_hand, main_deck)
        else:
            hit_decision(player_hand, main_deck)
    else:
        hit_decision(player_hand, main_deck)
    return player_hand
        
def calculate_hand(hand):
    if len(hand) == 2:
        for i in hand:
            if i.card_num == 1:
                Ace = True
            else:
                Ace = False
            if i.card_num == 9 or i.card_num == 10 or i.card_num == 11 or i.card_num == 12:
                Ten = True
            else:
                Ten = False
        if Ace == True and Ten == True:
            hand_value = "bj"
        else:
            hand_value = 0
            for i in hand:
                hand_value = hand_value + i.card_point
            if 1 in hand and hand_value <= 10:
                hand_value = hand_value + 10 
            else:
                pass
    else:
        hand_value = 0
        for i in hand:
            hand_value = hand_value + i.card_point
        if 1 in hand and hand_value <= 10:
            hand_value = hand_value + 10 
        else:
            pass
    return hand_value
        
def check_winner(player_hand, dealer_hand):
    player_point = calculate_hand(player_hand)
    print(player_point)
    dealer_point = calculate_hand(dealer_hand)
    print(dealer_point)
    if player_point > 21:
        payout = 0
    elif player_point == dealer_point:
        payout = 1
    elif player_point == "bj":
        payout = 2.5
    elif dealer_point > 21 or player_point > dealer_point:
        payout = 2
    else:
        payout = 0
    return payout
        
def new_game():
    deck.clear()
    dealerhand.clear()
    playerhand.clear()
    #ask player if they want to a new game
    
def hit_decision(player_hand, main_deck):
    user_choice = input("do you want an additional card?[Y/N]")
    if user_choice == "Y":
        player_hand.move_random_card(main_deck)
        hand_value = calculate_hand(player_hand)
        print(hand_value)
        if hand_value < 21:
            hit_decision(player_hand, main_deck)
        else:
            pass               
    elif user_choice == "N":
        pass
    else:
        print("please answer [Y/N]")
        hit_decision(player_hand, main_deck)
    return player_hand

def split_decision(player_hand, main_deck):
    user_choice = input("do you want to split?[Y/N]")
    if user_choice == "Y":
        player_hand.move_rand_card(player_hand)
        for i in num_of_hands:
            deck.move_random_card(player.hand)
            player_turn(player.hand[i-1])
    elif user_choice == "N":
        if hand_value == 20 and 1 in hand or hand_value == 9 or 10:
            double_decision()
        else:
            hit_decision()
    else:
        print("please answer [Y/N]")
        split_decision()

def double_decision(player_hand, main_deck):
    user_choice = input("do you want to double down?[Y/N]")
    if user_choice == "Y":
        #player.acct_balance = player.acct_balance - player.bet
        #player.bet = player.bet * 2
        player_hand.move_random_card(main_deck)
    elif user_choice == "N":
        hit_decision()
    else:
        print("please answer [Y/N]")
        double_decision(player_hand, main_deck)            
           
def dealer_turn(player_hand, dealer_hand, main_deck):
    print("dealer_turn")
    player_point = calculate_hand(player_hand)
    if player_point > 21:
        pass
    else:
        dealer_point = calculate_hand(dealer_hand)
        print("dealer_point:")
        print(dealer_point)
        if 1 in dealer_hand and 6 in dealer_hand or dealer_point < 17:
            dealer_hand.move_random_card(main_deck)
            dealer_turn(player_hand, dealer_hand, main_deck)
        else:
            pass