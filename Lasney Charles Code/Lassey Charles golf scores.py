#This is the pseudo code for Lassey Charles

#The first step in the code is to set up the main module
def main():

    #Next we set up the array size
    array_size=10

    #Next we set up the array
    golf_scores_array=[0]*array_size

    #Next we get the golf scores
    golf_scores=golf_score_getter(golf_scores_array,array_size)

   
    #Next we will  sort the golf scores
    sorted_golf_scores=bubble_sorter(golf_scores,array_size)

	#Now we show all of the golf scores
    golf_score_shower(sorted_golf_scores)    
#This function will ask the user for all of the golf scores
def golf_score_getter(golf_scores_array,array_size):

    #First we will iterate through the values 1 to 10 with a range based for loop
    for golf_score_number in range(0,array_size):
        #We will input each golf score into each element of the array by setting each element in the array equal to an input statement
        golf_scores_array[golf_score_number]=int(input("Please input golf score number {}\n".format(golf_score_number+1)))
    return golf_scores_array
#This function will help us swap variables for the bubble sorting function
def swap(a,b):
    #First we will set the temporary variable equal to a
    temp=a
    #Next we will swap the a value with the b value
    a=b
    #Finally we will set b equal to the value of the temporary variable
    b=temp
    #This is where we will return the new a and b values
    return a,b    
#This will be the function that sorts the array using a bubble sort algorithm
def bubble_sorter(golf_scores_array,array_size):
    #The first step is to set the boolean condition to enter the while loop and check if we need to swap variables
    
    variable_swap_checker=True

    #Now we will enter the while loop
    while variable_swap_checker==True:
        #We need to set variable_swap_checker to false to break out of the while loop when the sequence is done being sorted
        variable_swap_checker=False
        #This is where we will iterate through the indices 0 to length of array -1
        for index in range(0,len(golf_scores_array)-1):
         #we are going to see if the value at position i is greater than the value at position i+1
            if golf_scores_array[index]>golf_scores_array[index+1]:
               #This is where the variable swapping will take place.
                golf_scores_array[index],golf_scores_array[index+1]=swap(golf_scores_array[index],golf_scores_array[index+1])
                #Next we need to set the variable swap checker equal to true to continue sorting the list when needed
                variable_swap_checker=True
    #This is where we will return the sorted golf scores array
    return golf_scores_array

#This function will show all of the golf scores
def golf_score_shower(golf_scores_array):
    # we will iterate through the golf scores array list by using for i in list  
    for golf_score_number,golf_score in enumerate(golf_scores_array):
        #What  enumerate will do is iterate through the list, and also generate a index value for each variable in the list at the same time
        print ("Golf Score {} is {}".format(golf_score_number+1,golf_score))

#This is where we will call the main function                
main()
