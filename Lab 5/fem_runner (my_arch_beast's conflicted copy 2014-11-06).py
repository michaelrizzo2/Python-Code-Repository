import geometry_routine as my_functions
import assembly_routine as my_assembly
x_array=my_functions.x_array_output(9,0,2)
#print "X Array"
#print "The x array is %s " %str(x_array)
amount_elements_in_array=my_functions.number_of_elements(x_array)
#print "Amount of elements"
#print "The amount of elements in the x array are %s " %str(amount_elements_in_array)
number_of_unknowns=my_functions.number_of_unknowns_output("dirichlett","neumann",len(x_array))
#print "Number of Unknowns"
#print "The number of unknowns for the x array are %s " %str(number_of_unknowns)
local_node_to_global_node_matrix=my_functions.local_node_to_global_node_converter(amount_elements_in_array,2)
#print "Local to global node array"
#print "The local to global node  for the x array are %s " %str(local_node_to_global_node_matrix)
unknown_node_array=my_functions.unknown_node_creator("dirichlett","neumann",len(x_array))
#print "Unknown Node Array"
#print "The unknown node array is %s " %str(unknown_node_array)
area_of_elements =my_functions.element_area_calculator(x_array)
#print "Area of the elements"
#print "the area of the elements is %s" % str(area_of_elements)
x_quadrature_points=my_functions.quadrature_point_calculator(x_array)
#print "X quadrature points"
#print "The x quadrature points are %s " % str(x_quadrature_points)
my_assembly.assembly_routine(x_array,amount_elements_in_array,number_of_unknowns,x_quadrature_points,local_node_to_global_node_matrix,area_of_elements,unknown_node_array)
