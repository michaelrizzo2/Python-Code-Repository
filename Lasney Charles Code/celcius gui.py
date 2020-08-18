from tkinter import *

#The first step will be to create the window
root=Tk()

#This will set the title of the gui
root.title("Celsius to Fahrenheit")

#Now we need to set the variables we will be using for the program
#we will now set up the variable to hold the celcius temperature
celsius_temperature=DoubleVar()
fahrenheit_result=StringVar()
#Now we will add the labels for the program( Labels will be used to hold the text)
celsius_label=Label(root,text="Celsius Temperature").grid(row=0,column=0)
fahrenheit_label=Label(root,text="Fahrenheit result").grid(row=1,column=0)
#Now we need to add the entry boxes for the celcius input and the fahrenheit output
celsius_input=Entry(root,textvariable=celsius_temperature).grid(row=0,column=1)
fahrenheit_output=Entry(root,textvariable=fahrenheit_result).grid(row=1,column=1)
#Now we need to build the function that will convert from celsius to fahrenheit
def celsius_to_fahrenheit_converter():
    #The first step will be to get the variable for the celsius temperature
    celsius=celsius_temperature.get()
    fahrenheit_results=fahrenheit_result.get()
    #Next we will convert celsius to fahrenheit
    fahrenheit=celsius*9/5+32
    #Next we will post the result in the fahrenheit output entry box
    fahrenheit_result.set("Fahrenheit result is %s"% str(fahrenheit))
#Finally we need to set the button to call the function to convert the celsius
#tempearture to a fahrenheit temperature
converter_button=Button(root,text="Convert",command=celsius_to_fahrenheit_converter).grid(row=2,column=0)
#This will keep the window open
root.mainloop()
