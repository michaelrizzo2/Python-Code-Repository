#Python'Game 
#Lasner Jean Charles
#April 28, 206
#This program designs to play game with multiple choices

import random

def menu():
    print("Please enter slection for game play:")
    print("Enter 1 to see rules")
    print ("Enter 2 for single player")
    print ("Enter 3 for two player")                               
    print ("Enter 4 quit game")
    selection=int(input("Please make your selection"))
    if selection==1:
        rules()
    if selection ==2:
        singlePlayer()
    elif selection ==3:
        twoPlayer()
    while selection==4:
        break
def rules():
    print("Paper beats rock")
    print("Rock beats scissors")
    print("Scissors cuts paper")
    menu()
def singlePlayer():
    print("Please make your weapon seliction")   
    print("Enter 1 for rock")
    print("Enter 2 for paper ")
    print("Enter 3 for scissors")
    playerWeapon=int(input("Enter selection:"))
    comp=random.randint (1,3)
    #display the  computer choice
    print("computer choice :", comp)
    #display gam drawn. message when same choice

    if (comp ==playerWeapon):
        print("Gam drawn. select again")
        menu()
    else:
       #Calling function to decide winner
       winner (comp,playerWeapon)

       #winner function
def winner(comp, playerWeapon):
    #rock and scissors choice
    if (comp==1 and playerWeapon==3):
        print("computer wins")
        print("The rock smashes scissors")
    elif (comp ==1 and playerWeapon ==2):
        print("User wins ")
        print("The paper wraps rock")

    elif (comp==2 and playerWeapon==1):
        print("Comp wins ")
        print("The paper wraps rock")
    elif (comp ==2 and playerWeapon==3):
        print("Computer wins ")
        print("Scissors cut paper")
    elif (comp ==3 and playerWeapon==1):
        print("User wins")
        print("The rock smashes scissors")
    elif (comp==3 and playerWeapon==2):
        print("Computer or wins")
        print("Scissors cut paper")
        
    #Calling the main function
    menu()
def twoPlayer():
    print("Enter 1 for rock")
    print("Enter 2 for paper")
    print("Enter 3 for scissors")

    player1=int(input("Player1 enter your seliction:"))
    player2=int(input("Player2 enter your selection:"))

    if (player1==player2):
        print("Game Drawn select again")
        twoPlayer()
    else:
        #This is where we will call the winner function
        winner(player1,player2)
            
  
def main():
    menu()
main()    
