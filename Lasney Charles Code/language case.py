#The first step of the program is to define the main function
def main():
    #This will print the welcome message
    print ("Select a language and i will say good morning\n")
    #The next step is to ask the user for the option they want
    option=int(input("Please input 1 for english,2 for italian,3 for spanish,4 for german,and 5 to quit the program"))
    #Next we need to be sure that we chose a valid option
    while option<1 or option>5:
        #This is where we will ask the user for a proper option
        option=int(input("You have not chosen a proper option.Please input 1 for english,2 for italian,3 for spanish,4 for german,and 5 to quit the program\n"))
    #Next we need to set up the python equivalent of a case structure which will be a dictionary(also called an associative array)
    #a dictionary in python will link a value to a key. In this case the key will be the option, and the value will be the message that we want to print based on the option.
    #This means that the value will be associated with the key.
    output_dictionary={1:"Hello",2:"buongiorno",3:"Buenos dias",4:"Guten morgen"}
    #This is where we will print the result from the dictionary if the option is a language that is chosen
    if option in range(1,5):
        print ("You have chosen option %s which is %s"% (str(option),str(output_dictionary[option])))
    #This is where we will quit the program
    while option==5:
        #This is where we print the exit message
        print ("Thank you for using the program, have a nice day.Program is now exiting")
        #This is where we will break out of the while loop and exit the program.
        break
    
#This is where we will call the main function    
main()
