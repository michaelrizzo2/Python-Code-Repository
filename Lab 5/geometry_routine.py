#!/usr/bin/python2
import numpy as np
from math import *
def input_gatherer():
    left_boundary_condition=raw_input("Please input the boundary condition for the left hand side\n")
    right_boundary_condition=raw_input("Please input the boundary condition for the right hand side\n")
    initial_x_value=input("Please input initial x value\n")
    final_x_value=input("Please input final x value\n")
    #number_of_nodes=input("please input the number of nodes you want in the x array\n")
    p_value=input("Please input the p value of 0 or 1\n")
    q_value=input("Please input the q value of 0 or 1\n")
    return left_boundary_condition,right_boundary_condition,initial_x_value,final_x_value,p_value,q_value

x_array_output= lambda number_of_x_nodes,left_endpoint,right_endpoint : np.linspace(left_endpoint,right_endpoint,number_of_x_nodes,endpoint=True)
number_of_elements=lambda array: len(array)-1
def number_of_unknowns_output(left_boundary_condition,right_boundary_condition,length_of_array):
    number_of_unknowns=length_of_array
    if left_boundary_condition=="dirichlett":
        number_of_unknowns-=1
    if right_boundary_condition=="dirichlett":
        number_of_unknowns-=1
    return number_of_unknowns
def local_node_to_global_node_converter(number_of_elements,local_nodes_per_global_node):
    local_to_global_node_matrix=np.zeros((number_of_elements,local_nodes_per_global_node))
    for i in range(0,number_of_elements):
        local_to_global_node_matrix[i,0]=i
        local_to_global_node_matrix[i,1]=i+1
    return local_to_global_node_matrix
def unknown_node_creator(left_boundary_condition,right_boundary_condition,number_of_nodes):
    unknown_node_array=[0]*number_of_nodes
    for i in range(0,number_of_nodes):
        if i is 0:
            if left_boundary_condition=="dirichlett":
                unknown_node_array[i]=-1
            else:
                unknown_node_array[i]=i
        elif i in range(1,number_of_nodes-1):
            unknown_node_array[i]=i
        else:
            if right_boundary_condition =="dirichlett":
                unknown_node_array[i]=-1
            else:
                unknown_node_array[i]=i

    return unknown_node_array
element_area_calculator=lambda x_array: [x_array[i+1]-x_array[i] for i in range(0,len(x_array)-1)]
quadrature_point_calculator=lambda x_array: [(x_array[i+1]+x_array[i])/2 for i in range(0,len(x_array)-1)]
def linear_basis_calculator(x_array,x_point,node_index):
    if node_index is 0:
        if x_point>x_array[node_index+1]:
            basis_function_result=0
        elif x_point  == x_array[node_index]:
            basis_function_result=1
        else:#x_point>x_array[node_index] and x_point<x_array[node_index+1]
            basis_function_result=(x_point-x_array[node_index+1])/(x_array[node_index]-x_array[node_index+1])
    elif node_index in range(1,len(x_array)-1):
        if x_point>x_array[node_index-1] and x_point<x_array[node_index]:
            basis_function_result=(x_point-x_array[node_index-1])/(x_array[node_index]-x_array[node_index-1])
        elif x_point == x_array[node_index]:
            basis_function_result=1
        elif x_point>x_array[node_index] and x_point<x_array[node_index+1]:
            basis_function_result=(x_point-x_array[node_index+1])/(x_array[node_index]-x_array[node_index+1])
        else:
            basis_function_result=0
    else:
        if x_point>x_array[node_index-1] and x_point<x_array[node_index]:
            basis_function_result=(x_point-x_array[node_index-1])/(x_array[node_index]-x_array[node_index-1])
        elif x_point  == x_array[node_index]:
            basis_function_result=1
        else:
            basis_function_result=0
    

    return basis_function_result

def derivative_basis_calculator(x_array,x_point,node_index):
    if node_index is 0:
        if x_point>x_array[node_index+1]:
            basis_derivative_result=0
        elif x_point  == x_array[node_index]:
            basis_derivative_result=0
        else:#x_point>x_array[node_index] and x_point<x_array[node_index+1]
            basis_derivative_result=1/(x_array[node_index]-x_array[node_index+1])
    elif node_index in range(1,len(x_array)-1):
        if x_point>x_array[node_index-1] and x_point<x_array[node_index]:
            basis_derivative_result=1/(x_array[node_index]-x_array[node_index-1])
        elif x_point == x_array[node_index]:
            basis_derivative_result=0
        elif x_point>x_array[node_index] and x_point<x_array[node_index+1]:
            basis_derivative_result=1/(x_array[node_index]-x_array[node_index+1])
        else:
            basis_derivative_result=0
    else:
        if x_point>x_array[node_index-1] and x_point<x_array[node_index]:
            basis_derivative_result=1/(x_array[node_index]-x_array[node_index-1])
        elif x_point  == x_array[node_index]:
            basis_derivative_result=0
        else:
            basis_derivative_result=0

    return basis_derivative_result

rhs_function=lambda  x_value:pow(pi,2)*sin(pi*x_value)
#rhs_function=lambda  x_value:1
