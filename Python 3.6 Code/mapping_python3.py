#how to use the map function 
#map (function to apply,list of inputs)
numbers=[1,2,3,4,5]
squarer=lambda x:pow(x,2)

a=list(map(squarer,numbers))

print (f'a is {a}')
