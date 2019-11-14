#!/usr/bin/python3

import random
from itertools import groupby

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = { nine: "9", ten: "10",jack: "J",queen: "Q",king: "K",ace: "A" }

player_score = 0
computer_score = 0


def game():
	print("The computer will help you throw your 5 dice")
	throws()
	return play_again()

def throws():
	roll_number = 5 #first throw = 5 random dice but reused later as user selected 
	dice_list = roll(roll_number)
	for i in range(len(sorted(dice_list))):
		print("Dice", i+1,":", names[dice_list[i]])
	result = hand(dice_list)
	print("You currently have", result)
 	
	while True:
		rerolls = int(input("How many dice do you want to throw again?"))
		try:
			if rerolls in (1,2,3,4,5):
				break
		except ValueError:
			pass
		print("Oops!, Please enter 0,1,2,3,4 or 5")
	if rerolls == 0:
		print("You finish with", result)
	else:
		roll_number = rerolls
		dice_rerolls = roll(roll_number)
		dice_changes = []
		print("Enter the dice number to reroll it")
		iterations = 0
		while iterations < rerolls:
			print("Iteratons", iterations)
			iterations = iterations + 1
			while True:
				selection = int(input(""))
				try:
					if selection in (1,2,3,4,5):
						break
				except ValueError:
					pass
				print("Oops!, Please enter 1,2,3,4 or 5")
			print(len(dice_changes))
			print(selection)
			dice_changes.append(selection - 1)
			print("You have changed dice", selection)
 		
		iterations = 0
		while iterations < rerolls:
			iterations = iterations + 1
			replacement = dice_rerolls[iterations-1]
			dice_list[dice_changes[iterations-1]] = replacement
 			
		sorted(dice_list)
		for i in range(len(dice_list)):
			print("Dice", i+1, ":", names[dice_list[i]])
 			
		result = hand(dice_list)
		print("You finish with", result)

def roll(roll_number):
	numbers = range(1, 7)
	dice = list() #range(1, roll_number)
	iterations = 0
	while iterations < roll_number:
		iterations = iterations + 1
		dice.append(random.choice(numbers))
	return dice

def hand(dice):
	dice_hand = [len(list(group))for key, group in groupby(sorted(dice))]

	dice_hand.sort(reverse=True)
	straight1 = [1,2,3,4,5]
	straight2 = [5,4,3,2,1]
	
	if dice == straight1 or dice == straight2:
		return "a straight!"
	elif dice_hand[0] == 5:
		return "five of a kind!"
	elif dice_hand[0] == 4:
		return "four of a kind!"
	elif dice_hand[0] == 3:
		if dice_hand[1] == 2:
			return "a full house!"
		else:
			return "three of a kind"
	elif dice_hand[0] == 2:
		if dice_hand[1] == 2:
			return "two pair"
		else:
			return "one pair"
	else:
		return "a high card."		

def play_again():
	answer = input("Would you like to play again? y/n: ")
	if answer in ("y", "yes"):
		return answer
	else:
		print("Goodbye")

def show_scores():
	global player_score, computer_score
	print("High Scores")
	print("Player: ", player_score)
	print("Computer: ", computer_score)

def start_game():
	print("Let's play a game of dice")
	
	while game():
		pass
	show_scores()

if __name__ == "__main__":
	start_game()