class Pet(object):

    def set_name(self, name):
        self.__name = name

    def set_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


# The main function
def main():

    # Create an empty object  with no attributes from the Pet class
    pets = Pet()
    # Prompt user to enter name, type, and age of pet
    name = input('What is the name of the pet: ')
    animal_type = input('What type of pet is it: ')
    age = int(input('How old is your pet: '))
    #This will set all of the parameters for the pet object
    pets.set_name(name)
    pets.set_type(animal_type)
    pets.set_age(age)
    print('This will be added to the records. ')
    print('Here is the data you entered:')
    print('Pet Name: ', pets.get_name())
    print('Animal Type: ', pets.get_animal_type())
    print('Age: ', pets.get_age())

main()
