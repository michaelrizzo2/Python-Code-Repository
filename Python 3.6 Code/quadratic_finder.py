from math import pow
#This is where we will get a,b, and c
def intro():
    print("==========================================")
    print("Welcome to the quadratic formula calculator")
    print("==========================================\n")

def my_continue():
    continue_input=input("Do you want to continue?\n")
    if continue_input in ["Yes","yes","no","No"]:
        return continue_input
    else:
        my_continue()

def quadratic_calculator():
    a=int(input("Please input the a value for the quadratic\n"))

    b=int(input("Please input the b value for the quadratic\n")) 

    c=int(input("Please input the c value for the quadratic\n")) 

    #We need to calculate the discriminant
    discriminant=pow(b,2)-4*a*c

    #This is where we wil calculate the roots
    if discriminant<0:
        print(f"root 1 is ({-b} plus i sqrt{discriminant/-1}) over {2*a}")
        print(f"root 2 is ({-b} minus i sqrt{discriminant/-1}) over {2*a}")

    elif discriminant>0:
        print(f"root 1 is ({-b} plus sqrt{discriminant}) over {2*a}")
        print(f"root 2 is ({-b} minus sqrt{discriminant}) over {2*a}")

    else:
        print(f"root  is {-b}  over {2*a}")
    continue_input=my_continue()
    if continue_input in ["Yes","yes"]:
        quadratic_calculator()
    else:
        quit()

def menu():
    intro()
    quadratic_calculator()


def quit():
    print("Have a good day")

menu()
