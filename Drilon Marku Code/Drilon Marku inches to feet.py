# declare constant
INCHES = 12

#_define functions_______________________________________________________
def feet_to_inches(feet):
    return feet * INCHES

#_main___________________________________________________________________
feet = int(input("Enter the number of feet you want to convert to inches: "))
print(feet)
print("There are, " + str(feet_to_inches(feet)) + " inches in " + str(feet) + " feet")
