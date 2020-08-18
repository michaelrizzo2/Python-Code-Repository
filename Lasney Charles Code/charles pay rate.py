#Payroll Program with Input Validation
#Lasner Jean Charles
#04/14/2016
# Display employee groos pay
#This program disign to calculate employee gross pay
#calculate the rate

def getRate():
     #Declare real rate
     rate= eval(input("Enter hourly rate"))
     while rate <7.50 or rate > 18.25:
          rate=eval(input ("Sorry must be a positive number between 7.50 and 18.25, please try again"))
     return rate
def calcHours():
     #Declare real hours
     hours=eval(input("Enter the hours worked:"))
     while hours < 0 or hours> 40:
          hours=eval(input("sorry must be positive number between 0 and 40, please try again"))
     return hours
          
#Calculate the gross pay
def showGrossPay(hours,rate):
       #Declare gross pay(the gross pay will be calculated by multipliying the rate times the number of hours.)
          gross=hours*rate
          print ("Employee gross pay : $", gross)         
          


#Inside the main function we will get the number of hours,pay rate, and also calculate the gross pay

def main():
    hours=calcHours()
    rate=getRate()
    showGrossPay(hours,rate)

main()
    

