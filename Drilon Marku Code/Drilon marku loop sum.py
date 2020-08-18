# This number list variable will hold the 5 values the user wants to add together into a list
number_list=[]

# This for loop will be used to ask the user for the 5 numbers they want to add together(the for loop will start at value 0 and go to 4)
# Every iteration in the for loop will be used to ask the user for another number
for number in range(0,5):
	# This will allow the user to input the number and convert the string input to an integer
	#  By default the input function in python 3 returns a string , to get an integer input use input variable=int(input(input message))
	number_to_add_to_list=int(input("Please input the number you want to add to the list\n"))
	#This will add the number to the list
	number_list.append(number_to_add_to_list)
#Next we will call the function with the number list we created to find the sum	
def listsum(numList):
	if len(numList)==1:
            return numList[0]
	else:
            return numList[0]+listsum(numList[1:])

print (listsum(number_list))

