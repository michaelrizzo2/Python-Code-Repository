#!/usr/bin/python2
#First we need to import the abstractmethod function and abcmeta function from the abc module
from abc import ABCMeta,abstractmethod

#Now we need to create the base abstract class
class Base(metaclass=ABCMeta):
    #This is where we will apply the decorator
    @abstractmethod
    #Now we will create the class method
    def foo(self):
        pass
    
    #Now we will apply the decorator function again
    @abstractmethod
    #We will create the class method
    def bar(self):
        pass

