#Python'Game 
#Lasner Jean Charles
#April 28, 206
#This program designs to play game with multiple choices

import random
def menu():
          print("Please enter slection for game play:")
          print ("Enter 1 for single player")
          print ("Enter 2 for two player")                               
          print ("Enter 3 quit game")
          selection=int(input("Please make your selection"))
if selection ==1:
          singlePlayer()
elif selection ==2:
          twoPlayer()

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
              menu()
            elif (Cmp ==1 and playerWeapon ==2):
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
                    print("Computer wins")
                    printz("Scissors cut paper")
                    else:
                        print("Invalid selection")
    #Calling the main function
def twoPlayer():
    print("Enter 1 for rock")
    print("Enter 2 for paper")
    print("Enter 3 for scissors")
    player1=int(input("Player1 enter your seliction:"))
    player2=int(input("Player2 enter your selection:"))

                if (Player1==1 and Player2==3):
                    print("Player1 wins")
                    print("The rock smashes scissors")

                    menu()
                    elif (Player1==1 and Player2==2):
                        print("Plyer2 wins")
                        print("The paper wraps rock")
                    elif (Player1==2 and Player2==2):
                        print("Player1 wins")
                        print("The paper wraps rock")
                    elif (Player1==2 and Player2==3):
                        print("Player2 wins")
                        print("Scisoors cut paper")
                    elif (PLayer1==3 and Player2==1):
                        print("Player2 wins")
                        print("The rock smashes the scissors")
                    elif (Player1==3 and Player2==2):
                        print("Player1 wins")
                        print("Scissors cut paper")
                    elif (Player==Player2):
                        print("Game Drawn select again")

                    else:
                        print("Invalid selection")
                    #calling the main function
                        menu()