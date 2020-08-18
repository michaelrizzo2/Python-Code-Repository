import pickle
import employee_class as my_employee
#This is where we will get all of the pickled variables
def employee_list_getter():
    #We need to open the file that contains the list of all of the employee data
    employee_data_file=open("employee_list.pickle","rb")
    employee_list=pickle.load(employee_data_file)
    #Now we need to close the file 
    employee_data_file.close()
    return employee_list
def employee_file_list_getter():
    #First we need to open the file containing the employee list
    employee_file_list=open("employee_file_list.pickle","rb")
    #Next we need to load the object in the file
    employee_files=pickle.load(employee_file_list)
    #Now we need to close the file
    employee_file_list.close()
    return employee_files
def employee_name_list_getter():
    #We need to open the file that contains the list of all of the employee data
    employee_name_file=open("employee_name_list.pickle","rb")
    #Now we need to load the contents of the employee file in to the employee list variable
    employee_name_list=pickle.load(employee_name_file)
    #Now we need to close the file 
    employee_name_file.close()
    return employee_name_list
#This will save all of the variable values to the list
def variable_pickler(employee_list,employee_file_list,variable):
    if  variable =="employee list":
        #This is where we will choose the file
        employee_list_file="employee_list.pickle"
        #We need to open the file
        employee_list_pickle_file=open(employee_list_file,"wb")
        #We need to pickle the list to the file
        pickle.dump(employee_list,employee_list_pickle_file)
        #This is where we will close the file
        employee_list_pickle_file.close()
    if variable=="employee names":
        #First we need to generate the list of employee names
        employee_name_list=[name[0] for name in employee_list]
        #Next we need to choose the file for the list of employee names to go
        employee_name_list_file="employee_name_list.pickle"
        #Now we need to open the file
        employee_name_list_pickle_file=open(employee_name_list_file,"wb")
        #Next we will pickle the list to a file
        pickle.dump(employee_name_list,employee_name_list_pickle_file)
        #Finally we will close the file
        employee_name_list_pickle_file.close()
    if variable=="employee file":
        #Next we need to create the file to write the list to the file
        employee_files_file="employee_file_list.pickle"
        #Now we need to open the file
        employee_files_pickle_file=open(employee_files_file,"wb")
        #Next we will pickle the list to the file
        pickle.dump(employee_file_list,employee_files_pickle_file)
        #Next we will close the file
        employee_files_pickle_file.close()
#This will create the employee
def employee_creator(employee_list=[],employee_file_list=[]):
    #we need to create the list of employees
    employee=my_employee.Employee()
    employee_list.append(employee.list_setter())
    employee_file_name=employee.file_setter()
    employee_file_list.append(employee_file_name)
    return employee_list,employee_file_list
#This will choose the mode
def mode_chooser():
    #First we are going to ask if the user is an admin or an employee
    user_mode=input("Please input admin or employee\n")
    #Next we need to validate the user mode
    if user_mode in ["admin","employee"]:
        pass
    else:
        user_mode=input("Please input admin or employee\n")
    return user_mode


