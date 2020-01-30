*Written in Python 3.7.5*

**Blackjack**

#Rules:
1 deck
1 player
Shuffle after every game
No hole card
Unlimited split within 1 deck
Double on hard 10/11
Dealer stops at hard 17

#Instruction:
Run main.py with Python

#Game-play: 
1. Enter your preferred name
2. Enter the amount of chips in millions of dollars you would like to buy (1 = 1 million dollars) and you have to at least buy 1000 (only accept integers)
3. Place your bet (min = 1, max = 100) (only accept integers)

*-->The game will deal you 2 and the dealer 1 card alternatively

4. Player Decision Phrase - A (PDPA)
	The game will print your hand and its points
	If you get a bj, the game will not ask for your decision

	Else, if your two cards are of equal points, the game will ask if you want to split (only accept "Y" as yes or "N" as no, without the quotation marks)
		if you choose to split, it will split your 2 cards into 2 seperate hands, deal you 1 card for your first hand and start at the PDPA
		until you finish both PDPA and PDPB for your first hand, and then move on to your second hand. (Same process applies to further spliting)
	
		if you choose not to split, it will continue to check if you are allowed to double down

	Else, if your hand has a hard 9 or hard 10 points, the game will ask if you want to double down (only accept "Y" as yes or "N" as no, without the quotation marks)
		if you choose to double down, it will deal you an additional card and double your bet amount, and you will skip PDPB
	
		if you choose not to double down, it will continue to take you to PDPB

5. Player Decision Phrase - B (PDPB)
	The game will ask if you want to hit another card for your hand(s)
		if you choose to have another card, the game will deal you an additional card
		it will check and display your new hand and its points
	
		if your hand has greater than 21 (burst) you will be taken to the reset phrase
		else it will go through PDPB again, until you choose not to have another card, reach 21 points, or burst
	
6. The game will now complete and display the outcome

7. The game will ask if you want another bj(only accept "Y" as yes or "N" as no, without the quotation marks)
		if you choose to have another bj, the game will start at *-->
	
		if you choose not to have another bj, the game will end
	





