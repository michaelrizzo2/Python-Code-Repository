from Tkinter import *
root=Tk()
#This will hold all the variables
billamount=DoubleVar()
tippercantage=DoubleVar()
tipamount=DoubleVar()
billtotal=DoubleVar()
#This will hold the labels for the entries
billamountlabel=Label(root,text="Bill amount is").grid(row=0,column=0)
tippercentagelabel=Label(root,text="tip percentage is").grid(row=1,column=0)
tipamountlabel=Label(root,text="tip amount is").grid(row=2,column=0)
billtotallabel=Label(root,text="Bill total is").grid(row=3,column=0)
#This will be for the entries
billamountlabel=Entry(root,textvariable=billamount).grid(row=0,column=1)
tippercentagelabel=Entry(root,textvariable=tippercantage).grid(row=1,column=1)
tipamountlabel=Entry(root,textvariable=tipamount).grid(row=2,column=1)
billtotallabel=Entry(root,textvariable=billtotal).grid(row=3,column=1)
#This function will calculate the tip amount and the total bill
def total_bill_calculator():
    bill_amount=billamount.get()
    tip_percentage=tippercantage.get()
    tipamount.set(round(bill_amount*tip_percentage,2))
    tip_amount =tipamount.get()
    billtotal.set(bill_amount+tip_amount)
button=Button(root,text="Test",command=total_bill_calculator).grid(row=4,column=0)
root.mainloop()