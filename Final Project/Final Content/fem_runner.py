#!/usr/bin/python2
from math import *
import twod_geometry_routine as my_functions
import numpy as np
import error_routine as my_error
import pylab as pl
import final_new_assembly  as my_assembly
beginning_x_value,final_x_value,beginning_y_value,final_y_value,top_boundary_condition,bottom_boundary_condition,left_boundary_condition,right_boundary_condition,number_of_nodes_per_element,p_value,q_value=my_functions.input_gatherer()
error_list=[]
nodes_list=[5*x for x in range(1,21)]
for number_of_nodes_in_x,number_of_nodes_in_y in zip(nodes_list,nodes_list):
    x_array,y_array=my_functions.x_y_array_creator(beginning_x_value,final_x_value,number_of_nodes_in_x,beginning_y_value,final_y_value,number_of_nodes_in_y)
    #print "X Array"
    #print "The x array is %s " %str(x_array)
    amount_of_elements_in_x,amount_of_elements_in_y=my_functions.number_of_elements(x_array,y_array)
    #print "Amount of elements"
    #print "The amount of elements in the x array are %s " %str(amount_elements_in_array)
    number_of_x_unknowns,number_of_y_unknowns=my_functions.x_y_unknown_node_count(x_array,y_array,top_boundary_condition,bottom_boundary_condition,left_boundary_condition,right_boundary_condition)
    #print "Number of Unknowns"
    #print "The number of unknowns for the x array are %s " %str(number_of_unknowns)
    local_node_to_global_node_matrix=my_functions.local_to_global_node_matrix_creator(amount_of_elements_in_x,amount_of_elements_in_y,number_of_nodes_per_element)
    #print "Local to global node array"
    #print "The local to global node  for the x array are %s " %str(local_node_to_global_node_matrix)
    unknown_node_array=my_functions.unknown_matrix_creator(number_of_nodes_in_x,number_of_nodes_in_y,top_boundary_condition,bottom_boundary_condition,left_boundary_condition,right_boundary_condition)
    #print "Unknown Node Array"
    #print "The unknown node array is %s " %str(unknown_node_array)
    area_of_elements=my_functions.area_element_calculator(x_array,y_array,amount_of_elements_in_x,amount_of_elements_in_y)
    #print "Area of the elements"
    #print "the area of the elements is %s" % str(area_of_elements)
    quadrature_points=my_functions.quadrature_point_calculator(x_array,y_array,amount_of_elements_in_y,amount_of_elements_in_x)
    x_point_list,y_point_list=my_functions.x_y_array_node_coordinate(x_array,y_array,len(x_array))
    mass,stiffness,rhs=my_assembly.assembly_routine(x_array,y_array,x_point_list,y_point_list,amount_of_elements_in_x,amount_of_elements_in_y,number_of_x_unknowns,number_of_y_unknowns,quadrature_points,local_node_to_global_node_matrix,area_of_elements,unknown_node_array)
#    print "MASS"
#    print mass
#    print "STIFFNESS"
#    print stiffness
#    print "RHS"
#    print rhs
    ##print p_value*stiffness_matrix+q_value*mass_matrix
    solution=np.linalg.solve(p_value*stiffness+q_value*mass,rhs)
 #   solution=np.reshape(solution,(number_of_x_unknowns,number_of_y_unknowns))
#    print solution
    exact_solution=np.array([sin(pi*x)*sin(pi*y) for x in x_array[1:-1] for y in y_array[1:-1]])
    error=my_error.error_routine(amount_of_elements_in_x,amount_of_elements_in_y,number_of_x_unknowns,x_array,y_array,x_point_list,y_point_list,local_node_to_global_node_matrix,solution,unknown_node_array) 
    error_list.append(error)
    ##print mass_matrix
    ##print stiffness_matrix
    ##print p_value*stiffness_matrix+q_value*mass_matrix
#    pl.xlabel("X Values")
#    pl.ylabel("Y Values")
#    pl.legend()
#    pl.contour(solution)
#    pl.title("-Laplacian u =f(x,y) %i nodes" % number_of_nodes_in_x)
#    pl.savefig("-Laplacian u =f(x,y) %i nodes"% number_of_nodes_in_y)
#    pl.show()
#    pl.clf()
error_rate=[log10(error_list[i]/error_list[i-1])/log10(2) for i in range(len(error_list))]
print error_rate
