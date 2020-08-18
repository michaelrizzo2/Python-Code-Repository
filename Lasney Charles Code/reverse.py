def name_string():

    #enter a sting

    name_string= input('Enter a string ')
    #Reverse the string
    reversed_string= name_string[: :-1]


    #Print the reversed string
    print(reversed_string)


def main():
    #This is where we will call the function to ask the user for the string and reverse the string.
    name_string()

main()
