from functools import reduce

n=int(input("Please input the number you want to find the factorial of\n"))

product=reduce((lambda x,y:x*y),[i for i in range(n,0,-1)])

print (f'the factorial of {n} is {product}')


