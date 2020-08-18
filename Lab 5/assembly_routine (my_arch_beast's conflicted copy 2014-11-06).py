#!/usr/bin/python2
import geometry_routine as my_functions2
import numpy as np
def assembly_routine(x_array,number_of_elements,number_of_unknowns,quadrature_points,local_to_global_node_array,area_element_array,unknown_node_array):
    rhs=np.zeros((1,number_of_unknowns))
    stiffness_matrix=np.zeros((number_of_unknowns,number_of_unknowns))
    mass_matrix=np.zeros((number_of_unknowns,number_of_unknowns))
    for i in range(0,number_of_elements):
        for quad_point in quadrature_points[i:i+1]:
            for lnode in local_to_global_node_array[i]:
                for rnode in local_to_global_node_array[i]:
                    #First we need to check if the node has a boundary condition
