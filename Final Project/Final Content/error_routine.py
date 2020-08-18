#!/usr/bin/python2
from math import *
import twod_geometry_routine as my_geometry
def error_routine(number_of_elements_in_x,number_of_elements_in_y,number_of_unknowns_in_x,x_array,y_array,x_point_array,y_point_array,local_to_global_node_array,solution,unknown_node_array):
    error=0
    for element in range(number_of_elements_in_x*number_of_elements_in_y):
        u_approximation=0
        x_a=local_to_global_node_array[element,0]
        x_b=local_to_global_node_array[element,1]
        y_a=local_to_global_node_array[element,0]
        y_b=local_to_global_node_array[element,2]
        x_quadrature_points=[((x_array[x_point_array[int(x_a)]]+x_array[x_point_array[int(x_b)]])*sqrt(3)-x_array[x_point_array[int(x_b)]]+x_array[x_point_array[int(x_a)]])/(2*sqrt(3)),((x_array[x_point_array[int(x_a)]]+x_array[x_point_array[int(x_b)]])*sqrt(3)+x_array[x_point_array[int(x_b)]]-x_array[x_point_array[int(x_a)]])/(2*sqrt(3))]
        y_quadrature_points=[((y_array[y_point_array[int(y_a)]]+y_array[y_point_array[int(y_b)]])*sqrt(3)-y_array[y_point_array[int(y_b)]]+y_array[y_point_array[int(y_a)]])/(2*sqrt(3)),((y_array[y_point_array[int(y_a)]]+y_array[y_point_array[int(y_b)]])*sqrt(3)+y_array[y_point_array[int(y_b)]]-y_array[y_point_array[int(y_a)]])/(2*sqrt(3))]
        quadrature_points=[[x,y] for x in x_quadrature_points for y in y_quadrature_points]
        for quad_point in quadrature_points:
            for test_node in local_to_global_node_array[element]:
               if unknown_node_array[int(test_node)] == -1.0:
                   continue
               else:
                   if unknown_node_array[0] ==-1.0:
                       u_approximation+=solution[(y_point_array[int(test_node)]-1)*number_of_unknowns_in_x+(x_point_array[int(test_node)]-1)]*my_geometry.linear_basis_calculator(x_array,quad_point[0],x_point_array[int(test_node)])*my_geometry.linear_basis_calculator(y_array,quad_point[1],y_point_array[int(test_node)])
                   else:
                       u_approximation+=solution[(y_point_array[int(test_node)]-1)*number_of_unknowns_in_x+(x_point_array[int(test_node)]-1)]*my_geometry.linear_basis_calculator(x_array,quad_point[0],x_point_array[int(test_node)])*my_geometry.linear_basis_calculator(y_array,quad_point[1],y_point_array[int(test_node)])

            error+=(u_approximation-sin(pi*quad_point[0])*sin(pi*quad_point[1]))**2*((x_array[x_point_array[int(x_b)]]-x_array[x_point_array[int(x_a)]])/2.0)*((y_array[y_point_array[int(y_b)]]-y_array[y_point_array[int(y_a)]])/2.0)
            print "error calculation"
            print len(solution)
            print error
    return sqrt(error)


