def hoursRate(): 
  inp = input ('Enter Hours: ') 
  hours = float(inp) 
  inp = input ('Enter Rate: ') 
  rate = float(inp) 
  print("Rate = $%.2f, Hours = %.0f" % (rate, hours)) 
  return (hours, rate) 

def validation(hours, rate): 
    while hours > 40 or hours < 0: 
        print("hours have to be between 0-40") 
        hours = int(input("hours worked: ")) 
    while rate > 18.25 or rate < 7.50: 
        print("ERROR: pay rate has to be between 7.50 to 18.25") 
        rate = float(input("pay rate: ")) 
    return (hours, rate) 

def calcIncome(hours, rate): 
    weeklypay = hours * rate 
    print("payrate is $%.2f" % (weeklypay)) 

def main(): 
    hours, rate = hoursRate() 
    hours, rate = validation(hours, rate) 
    calcIncome(hours, rate) 
    
main() 