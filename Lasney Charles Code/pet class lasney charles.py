#Pet Class
#Lasner Jean Charles
#April 24, 2016
#This program designs to create a class name pet.
class Pet(object):
    def setName(self,n):
            self.__n=n
            
    def setType (self, t):
            self.__t=t
            
    def setAge(self, a):
            self.__a= a
            
    def getName (self):
            return self.__n
        
    def getType (self):
            return self.__t
        
    def getAge (self):
            return self.__a
    
def main():
    #First we need to set the myPet object
    myPet=Pet()
    petName= input('Please enter your pets name')
    myPet.setName(petName)
    petType= input('Please enter your pets type.ie:Dog,Cat,Bird,Reptile')
    myPet.setType(petType)
    petAge=input ('Please enter your pets age')
    myPet.setAge(petAge)
    print(myPet.getName())
    print(myPet.getType())
    print(myPet.getAge())
main()
