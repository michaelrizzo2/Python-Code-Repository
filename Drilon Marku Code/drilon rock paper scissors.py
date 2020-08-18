#import random module
import random
#main function
def main():
    #intro message
    print("Let's play 'Rock, Paper, Scissors'!")
    menu()
def menu():
	print("Select 1 for rules")
	print("select 2 for one player game")
	print("Select 3 for two player game")
	#If else logic to call proper functions
	option=int(input("Please input the option you want"))
	if option==1:
		rules()
	if option==2:
		onePlayer()
	if option==3:
		twoPlayer()
def rules():
	print("Paper beats rock")
	print("rock beats scissors")
	print("scissors beats paper")
	restart()
def onePlayer():
	#first we need to ask for the player 1 input
	player1=user_guess()
	computer=computer_number()
	results(player1,computer)

def twoPlayer():
	#first we need to ask for the player 1 input
	player1=user_guess()
	player2=user_guess()
	results(player1,player2)
	
#computer_number function
def computer_number():
    #get a random number in the range of 1 through 3
    num = random.randint(1,3)
    weapon_list=["rock","paper","scissors"]
    #if/elif statement
    if num == 1:
        print("Computer chooses rock")
    elif num == 2:
        print("Computer chooses paper")
    elif num == 3:
        print("Computer chooses scissors")
    #return the number
    return weapon_list[num-1]

#user_guess function
def user_guess():
    #get the user's guess
    guess = input("Choose 'rock', 'paper', or 'scissors' by typing that word. ")
    #while guess == 'paper' or guess == 'rock' or guess == 'scissors':
    if is_valid_guess(guess):
        return guess
    else:
        print('That response is invalid.')
        user_guess()

def is_valid_guess(guess):
    if guess == 'rock' or 'paper' or 'scissors':
        status = True
    else:
        status = False
    return status

def restart():
    answer = input("Would you like to play again? Enter 'y' for yes or \
    'n' for no: ")
    #if/elif statement
    if answer == 'y':
        menu()
    elif answer == 'n':
        print("Goodbye!")
    else:
        print("Please enter only 'y' or 'n'!")
        #call restart
        restart()

#results function
def results(player1,player2):
    print (player1,player2)
    if player1=="rock" and player2=="scissors":
    	print ("Player 1 wins")
    elif player1=="paper" and player2=="rock":
    	print ("Player 1 wins")
    elif player1=="scissors" and player2=="paper":
    	print ("Player 1 wins")
    elif player2=="rock" and player1=="scissors":
    	print ("Player 2 wins")
    elif player2=="paper" and player1=="rock":
    	print ("Player 2 wins")
    elif player2=="scissors" and player1=="paper":
    	print ("Player 2 wins")
    else:
    	print ("TIE")
    restart()


main()
