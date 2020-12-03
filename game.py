#!/usr/bin/env python2.7

import random
#this is a [light] game of blackjack. The concept is not to have a perfect game - but instead to see where you would make adjustments to make it closer to perfect. Read through the code and update the commented sections. Run the code in the terminal to understand how the game works. 
#please read through the code and provide answers to the questions on lines 18, 80 and 99

#playRound plays a single round of blackjack 
def playRound(playBank, remainingCards): 
		playerBank = playBank
		cards = remainingCards
		print('Player bank is ' + str(playerBank))
		playerBet = input('Place your bet (10-100): ')
		if (playerBet >= 10 and playerBet <= 100) and (playerBet <= playerBank):
			playerBank = playerBank - playerBet
			print('Player bet is ' + str(playerBet) + '. Bank total is now ' +str(playerBank))
			playerHand=deal(cards)
			dealerHand=deal(cards)
			print('Dealer hand is ' + str(dealerHand)) #question 1: you should only show the second card from the dealer... update this code to do this.
			print('Your hand is ' + str(playerHand))
			hs = raw_input('Hit or Stay? (h/s): ')
			while hs == "h":
				playerHand = hit(cards, playerHand)
				print(playerHand)
				if countHand(playerHand) > 21:
					hs = "b"
				else:
					hs = raw_input('Hit or Stay? (h/s): ' )
			while countHand(dealerHand) < 17:
				dealerHand = hit(cards, dealerHand)
			print('Your hand is ' + str(playerHand))
			print('Dealer hand is ' + str(dealerHand))  
			playerScore = countHand(playerHand)
			dealerScore = countHand(dealerHand)
			if hs == "b":
				print('You have busted. Dealer wins.')
			elif playerScore == 21:
				playerBank+=(playerBet*2.5)
				print('You have blackjack. Your new total bank is ' + str(playerBank))
			elif ((dealerScore > playerScore) and (dealerScore <= 21)):
				print('You lose, dealer wins. Your new total bank is ' + str(playerBank))
			elif (dealerScore == playerScore):
				playerBank+=playerBet
				print('Draw! Your new total bank is ' + str(playerBank))
			else:
				playerBank+=(playerBet*2)
				print('You win. Your new total bank is ' + str(playerBank))
			return playerBank
		elif playerBet <= 10 or playerBet >= 100: 
			print('Bet must be between $10 and $100')
			playRound(playerBank)
		else:
			print('Bet must be less than Player Bank.')
			playRound(playerBank)

			
#deal takes the remaining deck of cards and deals 2 random cards to the player
def deal(remainingCards):
	cards = remainingCards
	playerHand = []
	for x in range(0,2,1):
		card=cards[random.randint(0,len(remainingCards)-1)]
		cards.remove(card)
		playerHand.append(card)
	return playerHand

#hit takes the given hand and adds a single random card to the hand and returns it
def hit(remainingCards, hand):
	deckSize=len(remainingCards)
	card=remainingCards[random.randint(0,deckSize-1)]
	remainingCards.remove(card)
	hand.append(card)
	return hand

#countHand calculates the total score of the hand. 
def countHand(hand):
	handCount=0
	for x in hand:
		if(x[0:1] == 'A'):
			handCount+=1
			#question 2: ace can sometimes be 11 and sometimes be 1... how would you code this? 
		elif(x[0:1] == '1' or x[0:1] == 'J' or x[0:1] == 'Q' or x[0:1] == 'K'):
			handCount+=10
		else:
			handCount+= int(x[0:1])
	return handCount

def main():
	playAgain="y"
	playBank=500
	while playAgain == "y":
		remainingCards = ["As", "Ah", "Ad", "Ac","2s", "2h", "2d", "2c","3s", "3h", "3d", "3c","4s", "4h", "4d", "4c","5s", "5h", "5d", "5c","6s", "6h", "6d", "6c","7s", "7h", "7d", "7c","8s", "8h", "8d", "8c","9s", "9h", "9d", "9c","10s", "10h", "10d", "10c","Js", "Jh", "Jd", "Jc","Qs", "Qh", "Qd", "Qc","Ks", "Kh", "Kd", "Kc"]
		playBank = playRound(playBank, remainingCards)
		if playBank < 10:
			print("Sorry, not enough funds to play again!")
			playAgain="n"
		else:
			playAgain = raw_input("Play another round? (y/n) ")

#question 3: this code isn't perfect... how would you test it? 

if __name__ == "__main__":
    main()









