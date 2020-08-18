#!/usr/bin/python2
import twod_geometry_routine as my_functions2
import numpy as np
def assembly_routine(x_array,y_array,number_of_elements_in_x,number_of_elements_in_y,number_of_unknowns_in_x,number_of_unknowns_in_y,quadrature_points,local_to_global_node_array,area_element_array,unknown_node_matrix):
    rhs=np.zeros((number_of_unknowns_in_x*number_of_unknowns_in_y,1))
    stiffness_matrix=np.zeros((number_of_unknowns_in_x*number_of_unknowns_in_y,number_of_unknowns_in_x*number_of_unknowns_in_y))
    mass_matrix=np.zeros((number_of_unknowns_in_y*number_of_unknowns_in_x,number_of_unknowns_in_x*number_of_unknowns_in_y))
    for element_number in range(0,number_of_elements_in_x*number_of_elements_in_y):
        for quad_point in quadrature_points[element_number:element_number+1]:
            for test_node in local_to_global_node_array[element_number]:
                if unknown_node_matrix[x_array[int(test_node)]] is -1:
                    continue
                else:
                    #This is where we will calculate the right hand side
                    if unknown_node_matrix[0,0] is -1:
                        rhs[int(test_node)-1]+=my_functions2.rhs_function(quad_point[0],quad_point[1])*my_functions2.linear_basis_calculator(x_array,quad_point[0],int(test_node))*my_functions2.linear_basis_calculator(y_array,quad_point[1],int(test_node))*area_element_array[int(test_node)]
                    else:
                        rhs[int(test_node)]+=my_functions2.rhs_function(quad_point[0],quad_point[1])*my_functions2.linear_basis_calculator(x_array,quad_point[0],int(test_node))*my_functions2.linear_basis_calculator(y_array,quad_point[1],int(test_node))*area_element_array[int(test_node)]
                for trial_node in local_to_global_node_array[element_number]:
                    if unknown_node_matrix[x_array[int(test_node)],y_array[int(trial_node)]] is -1:
                        continue
                    else:
                        #This is where we will determine the sizing
                        if unknown_node_matrix[0,0] is -1:
                            #This is where we will calculate the matrix values
                            stiffness_matrix[test_node-1,trial_node-1]+=((my_functions2.derivative_basis_calculator(x_array,quad_point[0],test_node)*my_functions2.derivative_basis_calculator(y_array,quad_point[1],trial_node)+my_functions2.derivative_basis_calculator(y_array,quad_point[1],test_node)*my_functions2.derivative_basis_calculator(x_array,quad_point[0],trial_node))*area_element_array[element_number])
                            mass_matrix[test_node-1,trial_node-1]+=my_functions2.linear_basis_calculator(x_array,quad_point[0],test_node)*my_functions2.linear_basis_calculator(y_array,quad_point[0],trial_node)*area_element_array[element_number]
                        else:
                            #This is where we will calculate the matrix values
                            stiffness_matrix[x_array[int(test_node)],y_array[int(trial_node)]]+=((my_functions2.derivative_basis_calculator(x_array,quad_point[0],int(test_node))*my_functions2.derivative_basis_calculator(y_array,quad_point[1],int(trial_node))+my_functions2.derivative_basis_calculator(y_array,quad_point[0],int(test_node))*my_functions2.derivative_basis_calculator(x_array,quad_point[0],int(trial_node)))*area_element_array[element_number])
                            mass_matrix[x_array[int(test_node)],y_array[int(trial_node)]]+=my_functions2.linear_basis_calculator(x_array,quad_point[0],int(test_node))*my_functions2.linear_basis_calculator(y_array,quad_point[0],int(trial_node))*area_element_array[element_number]
    return mass_matrix,stiffness_matrix,rhs
