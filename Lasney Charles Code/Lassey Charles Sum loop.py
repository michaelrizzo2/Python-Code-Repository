#This is where we will ask the user for the integer
user_integer=int(input("Please input the number you want to sum to    "))
#This is where we will validate the use input with a while loop and a function

def user_integer_validator(user_integer):
	while user_integer<0:
#This is where will ask the user for an positive integer
		user_integer=int(input("Please input a number greater than zero    "))
#This is where we will return the user integer
	return user_integer

#This is where we will call the user integer validation function and return the user integer variable
user_integer=user_integer_validator(user_integer)
#This is where we will set up the sum variable
sum_variable=0
#This is where we will set up the for loop
for i in range(1,user_integer+1):
#This is where we will add the for loop variable to the sum variable
	sum_variable=sum_variable+i

#This is where we will print the value of the sum 

print("The sum of the first {0} numbers is {1}".format(user_integer,sum_variable))
