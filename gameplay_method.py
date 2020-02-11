"""
This is where all the gameplay functions are.
"""
import deck

def player_turn(player, player_hand, main_deck):
    """
    Parameter: (player, player_hand - deck object stored inside player.hand, main_deck)
    This function contains every step from the player receiving a 2nd card to bursting or not hitting for his last hand
    """
    # dealer a 2nd card to player
    player_hand.move_random_card(main_deck)
    print("Your second card is " + player_hand[1].card_eng_name)
    hand_value = calculate_hand(player_hand)
    print("You have " + str(hand_value))
    #c heck if player got blackjack. If yes, no decision has to be made
    if hand_value == "bj":
        pass
    # check if player is currently having 2 cards in his hand. If yes, the hand may qualify for spliting and/or doubling down
    elif len(player_hand) == 2:
        # check if player's 2 cards have the same point value. If yes, the hand qualifies for spliting     
        if player_hand[0].card_point == player_hand[1].card_point:
            # ask player if they want to split and pass answer as a parameter into split_decision
            user_answer = user_choice("do you want to split?[Y/N]")
            split_decision(user_answer, player, player_hand, main_deck)
        # when player's 2 cards do not qualify for spilting, check if it qualifies for doubling down
        # 1st row checks if player hand has 20 points with an Ace, which can be interpreted as 10 points
        # 2nd row checks if player hand has 19 points with an Ace, which can be interpreted as 9 points
        # 3rd row checks if player hand has 9 or 10 points
        elif hand_value == 20 and player_hand[0].card_point == 1 or hand_value == 20 and player_hand[1].card_point ==1 \
        or hand_value == 19 and player_hand[0].card_point == 1 or hand_value == 19 and player_hand[1].card_point ==1 \
        or hand_value == 9 or hand_value == 10:
            # ask player if they want to double down and pass answer as a parameter into double_decision
            user_answer = user_choice("do you want to double down?[Y/N]")
            double_decision(user_answer, player, player_hand, main_deck)
        # when player's 2 cards do not qualify for doubleing down, proceed to ask player if they want an additional card
        else:
            hit_decision_loop(player, player_hand, main_deck)
    # when player has more than 2 cards, ask player if they want an additional card
    else:
        hit_decision_loop(player, player_hand, main_deck)
    # After player finsihed making all decision for his last hand
    return player_hand
        
def calculate_hand(hand):
    """
    Parameter: (hand - a deck object)
    This function calculate a hand's value, "bj" or in points
    """
    # check if a hand is a blackjack, "bj"
    # check if hand contains exactly 2 cards
    if len(hand) == 2:
        # check if there is an Ace in hand
        if hand[0].card_point == 1 or hand[1].card_point == 1:
            # check if there is a 10-point card in hand, yes set hand_value to 'bj"
            if hand[0].card_point == 10 or hand[1].card_point == 10:
                hand_value = "bj"
            # calculate hand with 2 cards and 1 card being ace
            else:
                hand_value = 0
                for i in hand:
                    hand_value = hand_value + i.card_point
                if hand_value <= 10:
                    hand_value = hand_value + 10
        # calculate hand points with 2 cards and no ace
        else:
            hand_value = 0
            for i in hand:
                hand_value = hand_value + i.card_point
    # calculate hand points with 3 cards or more
    else:
        hand_value = 0
        Ace = False
        for i in hand:
            hand_value = hand_value + i.card_point
            # find out whether there is an ace in hand
            if i.card_point == 1:
                Ace = True
            else:
                pass
        # adjust hand_value when there is an ace in hand
        if Ace == True and hand_value <= 10:
            hand_value = hand_value + 10 
        # no ace
        else:
            pass
    return hand_value
        
def check_winner(player, player_hand, dealer_hand):
    """
    Parameter: (player, player_hand, dealer_hand - deck object stored inside dealer.hand)
    This function compares the hands of players to dealers
    """
    # calculate player's and dealer's hand value
    player_point = calculate_hand(player_hand)
    print("you have " + str(player_point))
    dealer_point = calculate_hand(dealer_hand)
    print("the dealer has " + str(dealer_point))
    # check if player has a blackjack
    if player_point == "bj":
        # if dealer also has a blackjack, return bet amount to player's bankroll
        if dealer_point == "bj":
            payout = 1
            outcome = "it's a draw"
        # if dealer's hand is not a blackjack, add 2.5 times(1 bet amount + 1.5 payout) the bet amount to player's bankroll
        else:
            payout = 2.5
            outcome = "you won 1.5x with a bj"
    # player does not have a blackjack, and if player bursted or dealer has a blackjack, player lose bet, and return 0 to player's bankroll
    elif player_point > 21 or dealer_point == "bj":
        payout = 0
        outcome = "you lose"
    # if player's hand = dealer's hand, return bet amount to player's bankroll
    elif player_point == dealer_point:
        payout = 1
        outcome = "it's a draw"
    # player does not have blackjack and did not burst, and if dealer burst or player's hand is stronger than dealer's hand, 
    # add 2 times the bet amount to player's bankroll
    elif dealer_point > 21 or player_point > dealer_point:
        payout = 2
        outcome = "you won"
    # player lose and return 0 to player's bankroll
    else:
        payout = 0
        outcome = "you lose"
    # if player chose to double down, payout is multiplited by 2
    if player_hand.double == True:
        payout = payout * 2
    print(outcome)
    # adjust player's bankroll according to the multiple of payout above
    adjust_fund = player.bet * payout
    player.adjust_fund(adjust_fund)
    print("your bankroll is now " + str(player.acct_balance))
        
def new_game(player, dealer):
    """
    Parameter: (user_answer, player, dealer)
    This function clears player.hand, player.bet, and dealer.hand
    """
    player.hand.clear()
    player.bet = 0
    dealer.hand.clear()
    
def hit_decision(user_answer, player, player_hand, main_deck):
    """
    Parameter: (player's answer, player, player_hand, main_deck)
    This function deals an additional card to player_hand or calculate and save the hand's point, and return player_hand
    """
    if user_answer == "Y":
        player_hand.move_random_card(main_deck)        
    else:
        hand_value = calculate_hand(player_hand)
        player.add_hand_value(hand_value)
    return player_hand

def split_decision(user_answer, player, player_hand, main_deck):
    """
    Parameter: (user_answer, player, player_hand, main-deck)
    This function will split the player's hand if user_answer is "Y", or it will check whether doubling down is possible, or it will
    proceed to hit_decision_loop
    """
    if user_answer == "Y":
        # create a new deck object - split_hand
        split_hand = deck.Deck()
        # move 1 card from player_hand to the split_hand
        split_hand.move_random_card(player_hand)
        # add split_hand into player's hand list
        player.add_deck(split_hand)
        # read the bet_amount of the current round
        bet_amount = player.bet
        # minus the bet_amount from player's bankroll
        player.adjust_fund(-bet_amount)
        # go back to the beginning of player_turn with the current player_hand
        player_turn(player, player_hand, main_deck)
    # check if player_hand has 2 5's (at this point all hands must be pairs, so only 5's can be doubled)
    elif player_hand[0] == 5:
        user_choice = user_choice("do you want to double down?[Y/N]")
        double_hand(player, player_hand, main_deck)
    # put player into hit_decision_loop
    else:
        hit_decision_loop(player, player_hand, main_deck)
    
def double_decision(user_answer, player, player_hand, main_deck):
    """
    Parameter: (user-answer, player, player_hand, main_deck)
    This function double a player's ahnd if user_answer is "Y", or it will procedd to hIt_decision_loop
    """
    if user_answer == "Y":
        # read the bet_amount of the current round
        bet_amount = player.bet
        # minus the best-amount from player's bankroll
        player.adjust_fund(-bet_amount)
        # deal 1 card to player_hand from main_deck
        player_hand.move_random_card(main_deck)
        # print the 3rd card player received 
        print(player_hand[2].card_eng_name)
        # calculate and add hand_value to player.hand_value
        hand_value = calculate_hand(player_hand)
        player.add_hand_value(hand_value)
        # change player_hand.double to True so 2x will be added/minused from bankroll in check_winner for the corresponding hand
        player_hand.double = True
    # put player into hit_decision_loop
    else:
        hit_decision_loop(player, player_hand, main_deck)
           
def dealer_turn(player_hand, dealer_hand, main_deck):
    """
    Parameter: (player_hand, dealer_hand, main_deck)
    This function is the procedure that a dealer follows depending on different situations
    """
    # print the card(s) in the dealer's hand and its total points
    print("the dealer's hand is as follow:")
    dealer_hand.hand_reader()
    player_point = calculate_hand(player_hand)
    # check if player has a blackjack
    if player_point == "bj":
        # check if dealer_hand has an Ace or a 10-point card
        if dealer_hand[0].card_point == 1 or dealer_hand[0].card_point == 10:
            # deal a card to dealer_hand from main_deck
            dealer_hand.move_random_card(main_deck)
            # print the updated dealer_hand
            dealer_hand.hand_reader()
        # pass if dealer has no chance to get a blackjack
        else:
            pass  
    # check if player bursted
    elif player_point > 21:
        pass
    # may be good to have a seperate function here so loop will skip the above 
    else:
        # calculate and print dealer_point
        dealer_point = calculate_hand(dealer_hand)
        print("the dealer has " + str(dealer_point))
        # if dealer has blackjack
        if dealer_point == "bj":
            pass
        # if dealer has less than 17 points
        elif dealer_point < 17:
            # deal a card to dealer_hand from main_deck
            dealer_hand.move_random_card(main_deck)
            # start over at the beginning of dealer_turn with the updated dealer_hand
            dealer_turn(player_hand, dealer_hand, main_deck)
        # if dealer has exactly 17 points
        elif dealer_point == 17:
            # check if if it is a hard or soft 17
            if dealer_hand[0].card_point == 1 or dealer_hand[1].card_point == 1:
                if dealer_hand[0].card_point == 6 or dealer_hand[1].card_point == 6:
                    # deal a card to dealer_hand from main_deck
                    dealer_hand.move_random_card(main_deck)
                    # start over at the beginning of dealer_turn with the updated dealer_hand
                    dealer_turn(player_hand, dealer_hand, main_deck)
                else:
                    pass
            else:
                pass
        else:
            pass
            
def user_choice(question):
    """
    Parameter: (question)
    This function print the str passed in as the parameter, prompt the user for a "Y" or "N" input, and return the answer
    """
    user_answer = input(question)
    if user_answer == "Y" or user_answer =="N":
        pass
    # if user entered anything other than "Y" or "N"
    else:
        print("please answer [Y/N]")
        # ask again
        user_answer = user_choice(question)
    return user_answer
    
def hit_decision_loop(player, player_hand, main_deck):
    """
    Parameter: (player, player_hand, main_deck)
    This function allows player to hit until the current hand burst or player wants to pass
    """
    while True:
        # ask if player wants an additional card
        user_answer = user_choice("do you want an additional card?[Y/N]")
        # store the return value of hit_decision  in player_hand
        player_hand = hit_decision(user_answer, player, player_hand, main_deck)
        # calculate and print
        hand_value = calculate_hand(player_hand)
        print("you have " + str(hand_value))   
        # check if player bursted or wants to pass
        if hand_value > 21 or user_answer == "N":
            break
        else:
            continue