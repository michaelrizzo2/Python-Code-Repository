#!/usr/bin/python2
from math import *
import geometry_routine as my_functions
import error_routine as my_error
import numpy as np
import pylab as pl
import new_assembly_routine as my_assembly
left_boundary_condition,right_boundary_condition,initial_x_value,final_x_value,p_value,q_value=my_functions.input_gatherer()
error_list=[]
for number_of_nodes in [5,9,17,33,65,127]:
        x_array=my_functions.x_array_output(number_of_nodes,initial_x_value,final_x_value)
        #print "X Array"
        #print "The x array is %s " %str(x_array)
        amount_elements_in_array=my_functions.number_of_elements(x_array)
        #print "Amount of elements"
        #print "The amount of elements in the x array are %s " %str(amount_elements_in_array)
        number_of_unknowns=my_functions.number_of_unknowns_output(left_boundary_condition,right_boundary_condition,len(x_array))
        #print "Number of Unknowns"
        #print "The number of unknowns for the x array are %s " %str(number_of_unknowns)
        local_node_to_global_node_matrix=my_functions.local_node_to_global_node_converter(amount_elements_in_array,2)
        #print "Local to global node array"
        #print "The local to global node  for the x array are %s " %str(local_node_to_global_node_matrix)
        unknown_node_array=my_functions.unknown_node_creator(left_boundary_condition,right_boundary_condition,len(x_array))
        #print "Unknown Node Array"
        #print "The unknown node array is %s " %str(unknown_node_array)
        area_of_elements =my_functions.element_area_calculator(x_array)
        #print "Area of the elements"
        #print "the area of the elements is %s" % str(area_of_elements)
        x_quadrature_points=my_functions.quadrature_point_calculator(x_array)
        #print "X quadrature points"
        #print "The x quadrature points are %s " % str(x_quadrature_points)
        mass_matrix,stiffness_matrix,rhs=my_assembly.assembly_routine(x_array,amount_elements_in_array,number_of_unknowns,x_quadrature_points,local_node_to_global_node_matrix,area_of_elements,unknown_node_array)
        #print p_value*stiffness_matrix+q_value*mass_matrix
        solution=np.linalg.solve(p_value*stiffness_matrix+q_value*mass_matrix,rhs)
        error=my_error.error_routine(amount_elements_in_array,x_array,local_node_to_global_node_matrix,solution,unknown_node_array)
        print error
        error_list.append(error)
        #print mass_matrix
        #print stiffness_matrix
        #print p_value*stiffness_matrix+q_value*mass_matrix
        pl.plot([x for x in x_array[1:-1]],solution,label="Fem Solution")
        pl.hold(True)
        pl.plot([x for x in x_array[1:-1]],[sin(pi*x) for x in x_array[1:-1]],label="Exact Solution")
        pl.xlabel("X values from 0 to 1")
        pl.ylabel("Y values")
        pl.title("%i nodes from 0 to 1" % number_of_nodes)
        pl.legend()
        pl.savefig("%i nodes 0 to 1.png" % number_of_nodes)
        pl.show()
convergence_list=[log10(error_list[i]/error_list[i+1])/log10(2) for i in range(0,len(error_list)-1)]
print  convergence_list
