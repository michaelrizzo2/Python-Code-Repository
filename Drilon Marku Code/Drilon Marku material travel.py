#The formula to calculate distance is d=rt

#The first step is to ask the user for the type of the material they want to go through.must return a string.
material=input('Please input air,water, or steel for the material you want to go through.\n')
#Next we need to get the speed of sound traveling through the material.
def speed_of_sound_through_material(material):
    if material=="air":
        return 1100#This will be in feet per second
    if material=="water":
        return 4900#This will also be in feet per second
    if material=="steel":
        return 16400#This will also be in feet per second

#Next we will call the previous function to get the rate at which sound will travel through the naterial.
sound_travel_rate=speed_of_sound_through_material(material)
#Next we need to ask the user how many seconds they want the sound to travel through the material.We want the user to have the option to input decimal values for seconds seconds(2.33,3.45,etc)
number_of_seconds=float(input("Please input the number of seconds you want sound to travel through the material\n"))

#Finally we create the function that will calculate the distance we went through the material
def distance_finder(sound_travel_rate,number_of_seconds):
    distance_travelled=sound_travel_rate*number_of_seconds
    print ("The distance travelled is {}".format(distance_travelled))


#Now we call the function to get the distance travelled through the material
distance_finder(sound_travel_rate,number_of_seconds)