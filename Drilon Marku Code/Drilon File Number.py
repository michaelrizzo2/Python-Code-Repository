def main():
    total=0
    numbers= open('numbers.txt', 'r')

    for line in numbers:
   	 for number in line:
        	if str(number)in "0123456789":
                    total+=int(number)
                    print (total)
    #close the file
    numbers.close()

#call main fucntion
main() 
