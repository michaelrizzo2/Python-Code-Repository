#This will show us how to use the filter functino in python 

number_list=[i for i in range(-5,6)]

output_list=list(filter(lambda x: x<0,number_list))

print (f'The output list is {output_list}')
