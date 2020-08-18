
Sunday = int(input("Enter the store sales for Sunday: "))
Monday = int(input("Enter the store sales for Monday: "))
Tuesday = int(input("Enter the store sales for Tuesday: "))
Wednesday = int(input("Enter the store sales for Wednesday: "))
Thursday = int(input("Enter the store sales for Thursday: "))
Friday = int(input("Enter the store sales for Friday: "))
Saturday = int(input("Enter the store sales for Saturday: "))

store_week_sales = [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]
#Set up total sales variable
total_sales=0
#Iterate through the list and add each value in the list to the total sales variable
for sale_amount in store_week_sales:
    #total_sales+=sale_amount is the same as total_sales=total_sales+sum_amount
    total_sales+=sale_amount
#Print out the total sales
print ("total sales is {0}".format(str(total_sales)))
