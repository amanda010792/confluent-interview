#!/usr/bin/env python2.7

import random
#this is a [light] game of blackjack. The concept is not to have a perfect game - but instead to see where you would make adjustments to make it closer to perfect. Read through the code and update the commented sections. Run the code in the terminal to understand how the game works. 

def main():

	def playRound(playBank): 
		playerBank = playBank
		print('Player bank is ' + str(playerBank))
		playerBet = input('Place your bet (10-100): ')
		if (playerBet >= 10 and playerBet <= 100) and (playerBet <= playerBank):
			playerBank = playerBank - playerBet
			print('Player bet is ' + str(playerBet) + '. Bank total is now ' +str(playerBank))
			playerHand=deal()
			dealerHand=deal()
			print('Dealer hand is ' + dealerHand[0] + " " + dealerHand[1])
			print('Your hand is ' + playerHand[0] + " " + playerHand[1])
			hs = raw_input('Hit or Stay? (h/s): ')
			while hs == "h":
				playerHand = hit(remainingCards, playerHand)
				print(playerHand)
				if countHand(playerHand) > 21:
					hs = "b"
				else:
					hs = raw_input('Hit or Stay? (h/s): ' )
			while countHand(dealerHand) < 17:
				dealerHand = hit(remainingCards, dealerHand)
			print('Your hand is ' + str(playerHand))
			print('Dealer hand is ' + str(dealerHand)) #question 1: you should only show the second card from the dealer... update this code to do this. 
			if hs == "b":
				print('You have busted. Dealer wins.')
				return playerBank
			elif ((countHand(dealerHand) > countHand(playerHand)) and (countHand(dealerHand) <= 21)):
				print('You lose, dealer wins. Your new total bank is ' + str(playerBank))
				return playerBank
			elif ((countHand(dealerHand)) == countHand(playerHand)):
				playerBank+=(playerBet)
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

	def deal():
		playerHand = []
		for x in range(0,2,1):
			card=remainingCards[random.randint(0,len(remainingCards)-1)]
			remainingCards.remove(card)
			playerHand.append(card)
		return playerHand


	def hit(remainingCards, playerHand):
		deckSize=len(remainingCards)
		card=remainingCards[random.randint(0,deckSize-1)]
		remainingCards.remove(card)
		playerHand.append(card)
		return playerHand

	def countHand(playerHand):
		handCount=0
		for x in playerHand:
			if(x[0:1] == 'A'):
				handCount+=1
				#question 2: ace can sometimes be 11 and sometimes be 1... how would you code this? 
			elif(x[0:1] == '1' or x[0:1] == 'J' or x[0:1] == 'Q' or x[0:1] == 'K'):
				handCount+=10
			else:
				handCount+= int(x[0:1])
		return handCount
	
	playAgain="y"
	playBank=500
	while playAgain == "y":
		remainingCards = ["As", "Ah", "Ad", "Ac","2s", "2h", "2d", "2c","3s", "3h", "3d", "3c","4s", "4h", "4d", "4c","5s", "5h", "5d", "5c","6s", "6h", "6d", "6c","7s", "7h", "7d", "7c","8s", "8h", "8d", "8c","9s", "9h", "9d", "9c","10s", "10h", "10d", "10c","Js", "Jh", "Jd", "Jc","Qs", "Qh", "Qd", "Qc","Ks", "Kh", "Kd", "Kc"]
		playBank = playRound(playBank)
		if playBank < 10:
			print("Sorry, not enough funds to play again!")
			playAgain="n"
		else:
			playAgain = raw_input("Play another round? (y/n) ")

#question 3: this code isn't perfect... how would you test it? 

if __name__ == "__main__":
    main()









