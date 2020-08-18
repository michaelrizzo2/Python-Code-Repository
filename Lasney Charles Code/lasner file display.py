#File Display

#Lasner Jean Charles

#April 17,2016

#This program disigns to read files from the the computer's disk.

def main():

    #Declare InputFile "number.dat"
    numbers_file=open("numbers.dat", "r")
    #This is where we will iterate through the numbers file
    for number in numbers_file:
        #This is where we will print each of the numbers
        print ("Number is %s\n" % number)

    numbers_file.close()

main() 
