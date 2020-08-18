#Recursive Multiplication
#Lasner Jean Charles
#April 20,2016
#This program disigns to create a recursive a function with two arguments

def getResult(x, y):
    if x==0 or y==0:
        return 0
    else:
        return x*getResult(x, y-1)

def main():
    #This is where we will call our getResult function
    recursive_result=getResult(2,3)
    print (recursive_result)

main()

