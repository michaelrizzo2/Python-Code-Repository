class Employee(object):
    def __init__(self):
        #We need the name of the employee,employee id,password,user name,email address, and physical address
        self.employee_name=raw_input("Please input the name of the employee\n")
        self.employee_id=raw_input("please enter the employee id\n")
        self.employee_username=raw_input("please enter the employee username\n")
        self.employee_password=raw_input("please enter the employee password\n")
        self.email_address=raw_input("Please input the email address of the employee\n")
        self.home_address=raw_input("Please input the home address of the employee\n")

    list_setter=lambda self:[self.employee_name,self.employee_id,self.employee_username,self.employee_password,self.email_address,self.home_address]

    def file_setter(self):
        #We need to create a list of descriptors for each of the pieces of data
        data_descriptor_list=["Name: ","Employee ID: ","User Name: ","Password: ","Email Address: ","Home Address: "]
        #First we need to create the file
        employee_data_output_file="%s_employee_information.txt" %self.employee_name
        employee_file=open(employee_data_output_file,"a")
        #Now we write the data to each file
        for data,descriptor in zip(self.list_setter(),data_descriptor_list): 
            employee_file.write("%s   %s\n\n" % (str(descriptor),str(data)))
        employee_file.close() 
        return employee_data_output_file   
