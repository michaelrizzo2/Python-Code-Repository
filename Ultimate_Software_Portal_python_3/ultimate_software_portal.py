import os as my_os
import ultimate_software_portal_library as my_library
#Now we need to choose the proper option
def first_time_setup():
    #This will ask the admin for the number of employees they want to add
    number_of_employees=int(input("Please input the number of employees you want to add\n"))
    #This will be the list for all of the employee data    
    employee_list=[]
    #This will set the employee file list
    employee_file_list=[]
    #This is where we will create all of the employees
    for employee_number in range(0,number_of_employees):
        employee_list,employee_file_list=my_library.employee_creator(employee_list,employee_file_list)
    #We need to put the employee list,employee name list and employee file list in their own file
    my_library.variable_pickler(employee_list,employee_file_list,"employee list")
    my_library.variable_pickler(employee_list,employee_file_list,"employee names")
    my_library.variable_pickler(employee_list,employee_file_list,"employee file")

def extra_options():
    option=input("Please input create, edit or delete\n")
    #This will validate the option
    if option in ["edit","create","delete"]:
        pass
    else:
        option=input("Please input create, edit or delete\n")
    #Now we will execute the action chosen    
    if option=="edit":
        employee_files=my_library.employee_file_list_getter()
        employee_name_list=my_library.employee_name_list_getter()
        #Next we ask for the employee that we want to edit
        employee=input("Please input the employee you want to edit\n")
        #Now we need to make sure the administrator chose a proper employee
        if employee in employee_name_list:
            pass
        else:
            employee=input("Please input the employee you want to edit\n")
        #We will now find the index of the employee
        employee_number=employee_name_list.index(employee)
        #we will now open the employee file
        my_os.system("vim {0}".format(str(employee_files[employee_number])))
    if option=="create":
        #We need to bring in the employee file list and employee list
        employee_files=my_library.employee_file_list_getter()
        employee_list=my_library.employee_list_getter()
        #Now we create the employee
        employee_list,employee_files=my_library.employee_creator(employee_list,employee_files)
        #Now we will store the new variables to the proper files
        my_library.variable_pickler(employee_list,employee_files,"employee list")
        my_library.variable_pickler(employee_list,employee_files,"employee names")
        my_library.variable_pickler(employee_list,employee_files,"employee file")
    if option=="delete":
        employee_files=my_library.employee_file_list_getter()
        employee_list=my_library.employee_list_getter()
        #We will ask the admin for the user they want to delete
        user_to_delete=input("Please input the employee you want to delete\n")
        employee_name_list=my_library.employee_name_list_getter()
        #We need to check if the admin chose a proper employee
        if user_to_delete in employee_name_list:
            pass
        else:
            user_to_delete=input("Please input the employee you want to delete\n")
        #Now we need to generate the index number the the employee holds so we can delete the employee    
        employee_number=employee_name_list.index(user_to_delete)
        #Now we need to remove the employee from the list
        employee_list.remove(employee_list[employee_number])
        #We need to delete the name of the employee from the list
        employee_name_list.remove(employee_name_list[employee_number])
        #Now we need to delete the file for the employee 
        my_os.system("rm %s" % str(employee_files[employee_number]))
        #Now we need to remove the file from the employee_list
        employee_files.remove(employee_files[employee_number])
        #Now we need to pickle the new values to the proper files
        my_library.variable_pickler(employee_list,employee_files,"employee list")
        my_library.variable_pickler(employee_list,employee_files,"employee names")
        my_library.variable_pickler(employee_list,employee_files,"employee file")
        restart()   

def admin():
    first_time=input("Please input yes for the first time or no for any other time\n")
    if first_time in ["yes","no"]:
        pass
    else:
        first_time=input("Please input yes for the first time or no for any other time\n")

    if first_time=="yes":
        #Call first time setup function and return employee list
        first_time_setup()
    elif first_time=="no":
        extra_options()
    restart()


def employee():
    #We need to get the employee name list ,employee file list, and employee list
    employee_file_list=my_library.employee_file_list_getter()
    employee_list=my_library.employee_list_getter()
    employee_name_list=my_library.employee_name_list_getter()
    #First we need to ask the employee for their name
    employee_name=input("Please input your name\n")
    #Next we need to get the employee index to validate the username and the password
    employee_index=employee_name_list.index(employee_name)
    #We will ask for the user name
    user_name=input("Please input your user name\n")
    #We will validate the user name
    if user_name==employee_list[employee_index][2]:
        pass
    else:
        user_name=input("Please input your user name\n")
    #We will ask the employee for the password
    password=input("Please input your password\n")
    #We will validate the password
    if password==employee_list[employee_index][3]:
        pass
    else:
        password=input("Please input your password\n")
    #Next we will open the employee file
    my_os.system("cat {0}".format( employee_file_list[employee_index]))
    #Next we will see if another employee wants to check their data
    restart()

def mode_caller(mode):
    if mode=="admin":
        admin()
    else:
        employee()

def restart():
    main()
#Now we need to set up the main function
def main():
    #First we need to get the mode we want
    mode=my_library.mode_chooser()
    mode_caller(mode)
main()    
