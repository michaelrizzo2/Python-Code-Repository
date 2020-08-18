def main(miles):
    while miles=="yes":
        kilometers=data()
        miles=calculate(kilometers)
        words(miles)
def data():
    print ("Enter kilometers please")
    kilometers=int(input())
    return kilometers

def calculate(kilometers):
    miles=kilometers*.6214
    return miles

def words(miles):
    print("The number of miles is {0:5.3f}".format(miles))
miles="yes"
main(miles)
