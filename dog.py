# dogs = list()
# append addds a single element to end of list
# dogs.append("German Shepard")
# dogs.append("Poodle")
# print(dogs)

class Dog:

    greeting = "Woof!"

    # bad to set name when dogs all have diff names
    # name = "Spot"
    # instead use __init__
    # set initial values when object is created
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)

# create an instance of dogs
# creating an object from class def is instantiation
# my_dog = Dog()
# my_dog.bark()

# check if code is run as module
# if __name__ == "__main__":
#     my_dog = Dog()
#     my_dog.bark()

# test name constructor
# my_dog = Dog("Spot")
# print (my_dog.name)

my_dog = Dog("Annie")
your_dog = Dog("Wyatt")
print(my_dog.name)
print(your_dog.name)
my_dog.bark()
your_dog.bark()

# built in variable to check where code is being run
# print(__name__)
