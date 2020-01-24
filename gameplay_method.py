def player_turn(player, player_hand, main_deck):
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
        if player_hand[0].card_point == player_hand[1].card_point:
            split_decision(player, player_hand, main_deck)
        #check double
        elif hand_value == 20 and 1 in player_hand or hand_value == 9 or hand_value == 10:
            double_decision(player, player_hand, main_deck)
        else:
            hit_decision(player, player_hand, main_deck)
    else:
        hit_decision(players, player_hand, main_deck)
    return player_hand
        
def calculate_hand(hand):
    if len(hand) == 2:
        if hand[0].card_point == 1 or hand[1].card_point == 1:
            if hand[0].card_point == 10 or hand[1].card_point == 10:
                hand_value = "bj"
            else:
                hand_value = 0
                for i in hand:
                    hand_value = hand_value + i.card_point
                if hand_value <= 10:
                    hand_value = hand_value + 10
        else:
            hand_value = 0
            for i in hand:
                hand_value = hand_value + i.card_point
    else:
        hand_value = 0
        Ace = False
        for i in hand:
            hand_value = hand_value + i.card_point
            if i.card_point == 1:
                Ace = True
            else:
                pass
        if Ace == True and hand_value <= 10:
            hand_value = hand_value + 10 
        else:
            pass
    return hand_value
        
def check_winner(player, player_hand, dealer_hand):
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
    player.acct_balance = player.acct_balance + player.bet * payout
        
def new_game(player, dealer):
    user_choice = input("do you want another game?[Y/N]")
    if user_choice == "Y":
        player.hand.clear()
        player.bet = 0
        dealer.hand.clear()
        return user_choice
    elif user_choice == "N":
        return user_choice
    else:
        print("please answer [Y/N]")
        new_game(player)
    #ask player if they want to a new game
    
def hit_decision(player, player_hand, main_deck):
    user_choice = input("do you want an additional card?[Y/N]")
    if user_choice == "Y":
        player_hand.move_random_card(main_deck)
        hand_value = calculate_hand(player_hand)
        print(hand_value)
        if hand_value < 21:
            hit_decision(player, player_hand, main_deck)
        else:
            player.add_hand_value(hand_value)
            pass               
    elif user_choice == "N":
        hand_value = calculate_hand(player_hand)
        player.add_hand_value(hand_value)
        pass
    else:
        print("please answer [Y/N]")
        hit_decision(player, player_hand, main_deck)
    return player_hand

def split_decision(player, player_hand, main_deck):
    user_choice = input("do you want to split?[Y/N]")
    if user_choice == "Y":
        import deck
        split_hand = deck.Deck()
        split_hand.move_random_card(player_hand)
        player.add_deck(split_hand)
        bet_amount = player.bet
        bet_amount = bet_amount*(-1)
        self.adjust_fund(bet_amount)
        gameplay_method.player_turn(player, player_hand, main_deck)
    elif user_choice == "N":
        if player_hand[0] == 5:
            double_decision(player, player_hand, main_deck)
        else:
            hit_decision(player, player_hand, main_deck)
    else:
        print("please answer [Y/N]")
        split_decision(player, player_hand, main_deck)

def double_decision(player, player_hand, main_deck):
    user_choice = input("do you want to double down?[Y/N]")
    if user_choice == "Y":
        #player.acct_balance = player.acct_balance - player.bet
        #player.bet = player.bet * 2
        player_hand.move_random_card(main_deck)
        hand_value = calculate_hand(player_hand)
        player.add_hand_value(hand_value)
    elif user_choice == "N":
        hit_decision(player, player_hand, main_deck)
    else:
        print("please answer [Y/N]")
        double_decision(player, player_hand, main_deck)            
           
def dealer_turn(player_hand, dealer_hand, main_deck):
    print("dealer_turn")
    player_point = calculate_hand(player_hand)
    if player_point == "bj" and dealer_hand[0].card_point != 1 and dealer_hand[0].card_point != 10:
        pass
    elif player_point > 21:
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