def main():
     #First we will ask the user for the number they want to sum up to
     numbers= int(input('Enter a number to add the sums: '))
     mysum = sum_num(numbers)
     print (mysum)
def sum_num(numbers):
          #The first step in the recursion process is to set a base value for the recursion process
          #The base recursion value will be for when the value called by the function is the lowest possible number.
          if numbers ==1:
               return 1
          else:
               #The second step of the recursion process will be to call the function with all of the other values beside 1
               return numbers+sum_num(numbers-1)
          
main()

#The code would work like this

#The user would want the sum of numbers from 1 to 6

#we would call the function with the highest possible value

#We would start off with 6+sum_function(5)

#sum_function(5) would become 5 +sum_function(4)

#sum_function(4) would become 4 +sum_function(3)

#sum_function(3) would become 3+sum_function(2)

#sum_function(2) would become 2+sum_function(1)

#sum_function(1) would become 1

#The final result would be 6+5+4+3+2+1, which would become 15
