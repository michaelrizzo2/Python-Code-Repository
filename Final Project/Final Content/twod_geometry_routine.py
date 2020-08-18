#!/usr/bin/python2
import numpy as np
from math import *
def input_gatherer():
    beginning_x_array_value=input("Please input the value for the beginning value of the x array\n")
    final_x_array_value=input("Please input the value for the final value of the x array\n")
    beginning_y_array_value=input("Please input the value for the beginning value of the y array\n")
    final_y_array_value=input("Please input the value for the final value of the y array\n")
    top_boundary_condition=raw_input("Please input the boundary condition for the top edge of the element\n")
    bottom_boundary_condition=raw_input("Please input the boundary condition for the bottom edge of the element\n")
    left_boundary_condition=raw_input("Please input the boundary condition for the left edge of the element\n")
    right_boundary_condition=raw_input("Please input the boundary condition for the right edge of the element\n")
    number_of_nodes_per_element=input("Please input number of nodes per element\n")
    p_value=input("Please input the  p value of 0 or 1\n")
    q_value=input("Please input the  q value of 0 or 1\n")
    return beginning_x_array_value,final_x_array_value,beginning_y_array_value,final_y_array_value,top_boundary_condition,bottom_boundary_condition,left_boundary_condition,right_boundary_condition,number_of_nodes_per_element,p_value,q_value

def x_y_array_creator(initial_x_value,final_x_value,number_of_nodes_in_x_array,initial_y_value,final_y_value,number_of_nodes_in_y_array):
    x_array=np.linspace(initial_x_value,final_x_value,number_of_nodes_in_x_array,endpoint=True)
    y_array=np.linspace(initial_y_value,final_y_value,number_of_nodes_in_y_array,endpoint=True)
    return x_array,y_array

def number_of_elements(x_array,y_array):
    number_of_x_elements=len(x_array)-1
    number_of_y_elements=len(y_array)-1
    return number_of_x_elements,number_of_y_elements

def x_y_unknown_node_count(x_array,y_array,top_boundary_condition,bottom_boundary_condition,left_boundary_condition,right_boundary_condition):
    number_of_x_unknowns=len(x_array)
    number_of_y_unknowns=len(y_array)

    if top_boundary_condition=="dirichlett":
        number_of_y_unknowns-=1
    
    if bottom_boundary_condition=="dirichlett":
        number_of_y_unknowns-=1

    if left_boundary_condition=="dirichlett":
        number_of_x_unknowns-=1
    
    if right_boundary_condition=="dirichlett":
        number_of_x_unknowns-=1
    return number_of_x_unknowns,number_of_y_unknowns

def unknown_matrix_creator(number_of_nodes_in_x_array,number_of_nodes_in_y_array,top_boundary_condition,bottom_boundary_condition,left_boundary_condition,right_boundary_condition):
    unknown_node_matrix=np.zeros((number_of_nodes_in_x_array,number_of_nodes_in_y_array))
    for x_index,x_node in enumerate(range(number_of_nodes_in_x_array)):
        for y_index,y_node in enumerate(range(number_of_nodes_in_y_array)):
            if y_node is 0:

                if left_boundary_condition=="dirichlett":
                    unknown_node_matrix[y_node,x_node]=-1
                else:
                    unknown_node_matrix[y_node,x_node]=y_index*number_of_nodes_in_x_array+x_index

            elif y_node is  number_of_nodes_in_y_array-1:

                if right_boundary_condition=="dirichlett":
                    unknown_node_matrix[y_node,x_node]=-1
                else:
                    unknown_node_matrix[y_node,x_node]=y_index*number_of_nodes_in_x_array+x_index

            elif x_node is 0:

                if bottom_boundary_condition=="dirichlett":
                    unknown_node_matrix[y_node,x_node]=-1
                else:
                    unknown_node_matrix[y_node,x_node]=y_index*number_of_nodes_in_x_array+x_index

            elif x_node is number_of_nodes_in_y_array-1:

                if top_boundary_condition=="dirichlett":
                    unknown_node_matrix[y_node,x_node]=-1
                else:
                    unknown_node_matrix[y_node,x_node]=y_index*number_of_nodes_in_x_array+x_index
            else:
                unknown_node_matrix[y_node,x_node]=y_index*number_of_nodes_in_x_array+x_index
    return np.reshape(unknown_node_matrix,number_of_nodes_in_x_array*number_of_nodes_in_y_array)

def local_to_global_node_matrix_creator(number_of_elements_in_x,number_of_elements_in_y,number_of_nodes_per_element):
    local_to_global_node_matrix=np.zeros((number_of_elements_in_x*number_of_elements_in_y,number_of_nodes_per_element))
    element=0
    inode=0
    for j in range(number_of_elements_in_x):
            for i in range(number_of_elements_in_y):
                    local_to_global_node_matrix[element,0]=inode
                    local_to_global_node_matrix[element,1]=inode+1
                    local_to_global_node_matrix[element,2]=inode+number_of_elements_in_x+1
                    local_to_global_node_matrix[element,3]=inode+number_of_elements_in_x+2
                    element+=1
                    inode=element+(element/number_of_elements_in_y)
    return local_to_global_node_matrix 

def area_element_calculator(x_array,y_array,number_of_x_elements,number_of_y_elements):
    area_of_elements=np.zeros((number_of_x_elements*number_of_y_elements,1))
    for y_node in range(len(y_array)-1):
        for x_node in range(len(x_array)-1):
            area_of_elements[y_node*number_of_y_elements+x_node]=(x_array[x_node+1]-x_array[x_node])*(y_array[y_node+1]-y_array[y_node])
    return area_of_elements

def quadrature_point_calculator(x_array,y_array,number_of_y_elements,number_of_x_elements):
    quad_points=np.zeros((number_of_x_elements*number_of_y_elements,2))
    for y_index,y_node in enumerate(range(len(y_array)-1)):
        for x_node in range(len(x_array)-1):
            x_point=(x_array[x_node+1]+x_array[x_node])/2
            y_point=(y_array[y_node+1]+y_array[y_node])/2
            quad_points[y_index*number_of_x_elements+x_node,0]=x_point
            quad_points[y_index*number_of_x_elements+x_node,1]=y_point
    return quad_points

def linear_basis_calculator(array,point,node_index):
    if node_index is 0:
        if point>array[node_index+1]:
            basis_function_result=0
        elif point  == array[node_index]:
            basis_function_result=1
        else:#point>array[node_index] and point<array[node_index+1]
            basis_function_result=(point-array[node_index+1])/(array[node_index]-array[node_index+1])
    elif node_index in range(1,len(array)-1):
        if point>array[node_index-1] and point<array[node_index]:
            basis_function_result=(point-array[node_index-1])/(array[node_index]-array[node_index-1])
        elif point == array[node_index]:
            basis_function_result=1
        elif point>array[node_index] and point<array[node_index+1]:
            basis_function_result=(point-array[node_index+1])/(array[node_index]-array[node_index+1])
        else:
            basis_function_result=0
    else:
        if point>array[node_index-1] and point<array[node_index]:
            basis_function_result=(point-array[node_index-1])/(array[node_index]-array[node_index-1])
        elif point  == array[node_index]:
            basis_function_result=1
        else:
            basis_function_result=0

    return basis_function_result

def derivative_basis_calculator(array,point,node_index):
    if node_index is 0:
        if point>array[node_index+1]:
            basis_derivative_result=0
        elif point  == array[node_index]:
            basis_derivative_result=0
        else:#point>array[node_index] and point<array[node_index+1]
            basis_derivative_result=1/(array[node_index]-array[node_index+1])
    elif node_index in range(1,len(array)-1):
        if point>array[node_index-1] and point<array[node_index]:
            basis_derivative_result=1/(array[node_index]-array[node_index-1])
        elif point == array[node_index]:
            basis_derivative_result=0
        elif point>array[node_index] and point<array[node_index+1]:
            basis_derivative_result=1/(array[node_index]-array[node_index+1])
        else:
            basis_derivative_result=0
    else:
        if point>array[node_index-1] and point<array[node_index]:
            basis_derivative_result=1/(array[node_index]-array[node_index-1])
        elif point  == array[node_index]:
            basis_derivative_result=0
        else:
            basis_derivative_result=0

    return basis_derivative_result

def x_y_array_node_coordinate(x_array,y_array,number_of_x_elements):
    x_point_list=[]
    y_point_list=[]
    for y_point in range(len(y_array)):
        for x_point in range(len(x_array)):
            x_point_list.append(x_point)
            y_point_list.append(y_point)
    return  x_point_list,y_point_list

rhs_function=lambda x_value,y_value: 2*pow(pi,2)*sin(pi*x_value)*sin(pi*y_value)
