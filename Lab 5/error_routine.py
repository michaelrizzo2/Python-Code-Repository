#!/usr/bin/python2
from math import *
import geometry_routine as my_geometry
def error_routine(number_of_elements,x_array,local_to_global_node_array,solution,unknown_node_array):
    error=0
    for element in range(number_of_elements):
        a=local_to_global_node_array[element,0]
        b=local_to_global_node_array[element,1]
        quadrature_points=[((x_array[a]+x_array[b])*sqrt(3)-x_array[b]+x_array[a])/(2*sqrt(3)),((x_array[a]+x_array[b])*sqrt(3)+x_array[b]-x_array[a])/(2*sqrt(3))]
        for quad_point in quadrature_points:
            u_approximation=0
            for test_node in local_to_global_node_array[element]:
               if unknown_node_array[int(test_node)] is -1:
                   continue
               else:
                   if unknown_node_array[0] is -1:
                       u_approximation+=solution[test_node-1]*my_geometry.linear_basis_calculator(x_array,quad_point,test_node)
                   else:
                       u_approximation+=solution[test_node]*my_geometry.linear_basis_calculator(x_array,quad_point,test_node)
            error+=(u_approximation-sin(pi*quad_point))**2*(x_array[b]-x_array[a])/2.0
    return sqrt(error)



