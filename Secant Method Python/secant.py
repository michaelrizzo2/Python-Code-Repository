#/usr/bin/python
from math import *
xnm1=input("Please input xnm1\n")
xn=input("Please input xn\n")
maxiterations=input("Please input max number of iterations\n")
print"Your xnm1 is %s  and your xn is %s" % (str(xnm1),str(xn))
tolerancecheck=1*pow(10,-6)
def secantfunction(x):
    y=exp(x)-12*x
    return y

fxproduct=secantfunction(xn)*secantfunction(xnm1)


if fxproduct>0:
    print "You have not found a root between %s and %s " %(str(xnm1) ,str(xn))
else:
    print "You have found a root between %s and %s " %(str(xnm1) ,str(xn))
    tolerance=10000000
    iterationcounter=0
    print "-------------------------------------------------------------"
    print "|| iterations"+"|| root     "+  "     || Function Value||"
    print "-------------------------------------------------------------"
    while tolerance>tolerancecheck and iterationcounter<maxiterations and xnm1-xn!=0:
        xnp1=xnm1-secantfunction(xnm1)*((xn-xnm1)/(secantfunction(xn)-secantfunction(xnm1)))
        print "||         "+str(iterationcounter)+         " ||"        +str(xnp1)+        " ||"+        str(secantfunction(xnp1))+"||"
        xnm1=xn
        xn=xnp1
        tolerance=xn-xnm1
        iterationcounter+=1
    print "-------------------------------------------------------------------"
    print "                                                                   "

