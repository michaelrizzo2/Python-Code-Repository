#!/usr/bin/python2
import geometry_routine as my_functions2
import numpy as np
def assembly_routine(x_array,number_of_elements,number_of_unknowns,quadrature_points,local_to_global_node_array,area_element_array,unknown_node_array):
    rhs=np.zeros((1,number_of_unknowns))
    stiffness_matrix=np.zeros((number_of_unknowns,number_of_unknowns))
    mass_matrix=np.zeros((number_of_unknowns,number_of_unknowns))
    for element_number in range(0,number_of_elements):
        for quad_point in quadrature_points[element_number:element_number+1]:
            for test_node in local_to_global_node_array[element_number]:
                for trial_node in local_to_global_node_array[element_number]:
                    if unknown_node_array[int(test_node)] is -1 or unknown_node_array[int(trial_node)] is -1:
                        continue
                    else:
                        #This is where we will determine the sizing
                        if unknown_node_array[0] is -1:
                            #This is where we will calculate the matrix values
                            #stiffness_matrix[test_node-1,trial_node-1]=my_functions2.derivative_basis_calculator(x_array,quad_point,test_node)*my_functions2.derivative_basis_calculator(x_array,quad_point,trial_node)
                            #print stiffness_matrix
                            mass_matrix[test_node-1,trial_node-1]=my_functions2.linear_basis_calculator(x_array,quad_point,test_node)*my_functions2.linear_basis_calculator(x_array,quad_point,trial_node)*area_element_array[element_number]
                            print mass_matrix
                        else:
                            #This is where we will calculate the matrix values
                            pass
