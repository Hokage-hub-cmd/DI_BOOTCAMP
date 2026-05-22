
#exercise 1: Cats

# Create the Pets class
class Pets():
    
    # Constructor: receives a list of animals
    def __init__(self, animals):
        self.animals = animals

    # Method to make all animals walk
    def walk(self):
        for animal in self.animals:
            print(animal.walk())


# Create the Cat class
class Cat():
    
    # Class attribute
    is_lazy = True

    # Constructor of the Cat class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Walk method
    def walk(self):
        return f'{self.name} is just walking around'


# Bengal class inheriting from Cat
class Bengal(Cat):
    
    # Sing method
    def sing(self, sounds):
        return f'{sounds}'


# Chartreux class inheriting from Cat
class Chartreux(Cat):
    
    # Sing method
    def sing(self, sounds):
        return f'{sounds}'



class Siamese(Cat):
    
    # Sing method
    def sing(self, sounds):
        return f'{sounds}'


# Create a Bengal cat object
bengal_cat = Bengal("Milo", 2)

# Create a Chartreux cat object
chartreux_cat = Chartreux("Luna", 3)

# Create a Siamese cat object
siamese_cat = Siamese("Bella", 1)

# Create a list containing all cat objects
all_cats = [bengal_cat, chartreux_cat, siamese_cat]


# Create a Pets object with the list of cats
sara_pets = Pets(all_cats)

sara_pets.walk()


#Exercise 2: Dogs


# Create the Dog class
class Dog():

    # Constructor to initialize attributes
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    # Method for barking
    def bark(self):
        return f"{self.name} is barking"

    # Method to calculate running speed
    def run_speed(self):
        return (self.weight / self.age) * 10

    # Method to determine the winner of a fight
    def fight(self, other_dog):

        # Calculate the power of each dog
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        # Compare powers
        if self_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}"

        elif self_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}"

        else:
            return f"{self.name} and {other_dog.name} are equally strong"




dog1 = Dog("Rocky", 3, 20)
dog2 = Dog("Max", 5, 25)
dog3 = Dog("Bella", 2, 15)




# Test bark method
print(dog1.bark())

# Test run_speed method
print(f"{dog2.name}'s speed is:", dog2.run_speed())

# Test fight method
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))



#exercise 3: Dogs Domesticated

# Import the random module
import random


class Dog():

    # Constructor to initialize attributes
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    # Method for barking
    def bark(self):
        return f"{self.name} is barking"

    # Method to calculate running speed
    def run_speed(self):
        return (self.weight / self.age) * 10

    # Method to determine the winner of a fight
    def fight(self, other_dog):

        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}"

        elif self_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}"

        else:
            return f"{self.name} and {other_dog.name} are equally strong"



class PetDog(Dog):

    # Constructor using inheritance
    def __init__(self, name, age, weight, trained=False):

        # Call the parent constructor
        super().__init__(name, age, weight)

        # Add the trained attribute
        self.trained = trained

    # Train the dog
    def train(self):

        # Print the bark message
        print(self.bark())

        # Set trained to True
        self.trained = True

    # Method for dogs playing together
    def play(self, *args):

        # Create a list of dog names
        dog_names = [self.name]

        # Add names of other dogs
        for dog in args:
            dog_names.append(dog.name)

        # Print the play message
        print(f"{', '.join(dog_names)} all play together")

    # Method for doing a random trick
    def do_a_trick(self):

        # Check if the dog is trained
        if self.trained:

            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]

            # Print a random trick
            print(f"{self.name} {random.choice(tricks)}")



# Create PetDog objects
dog1 = PetDog("Rocky", 3, 20)
dog2 = PetDog("Max", 5, 25)
dog3 = PetDog("Bella", 2, 15)

# Train dog1
dog1.train()

# Make dogs play together
dog1.play(dog2, dog3)

# Dog performs a trick
dog1.do_a_trick()




#Exercise 4: Family and Person Classes



class Person():

    # Constructor to initialize attributes
    def __init__(self, first_name, age):

        self.first_name = first_name
        self.age = age
        self.last_name = ""

    # Method to check if the person is 18 or older
    def is_18(self):

        if self.age >= 18:
            return True
        else:
            return False




class Family():

    # Constructor to initialize attributes
    def __init__(self, last_name):

        self.last_name = last_name
        self.members = []

    # Method to add a new family member
    def born(self, first_name, age):

        # Create a new Person object
        person = Person(first_name, age)

        # Assign the family last name
        person.last_name = self.last_name

        # Add the person to the members list
        self.members.append(person)

    # Method to check if a member is over 18
    def check_majority(self, first_name):

        # Search for the person in the members list
        for member in self.members:

            if member.first_name == first_name:

                # Check if the person is 18 or older
                if member.is_18():

                    print(
                        "You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )

                else:

                    print(
                        "Sorry, you are not allowed to go out with your friends."
                    )

    # Method to display family information
    def family_presentation(self):

        # Print the family last name
        print(f"Family name: {self.last_name}")

        # Print information about each member
        for member in self.members:

            print(f"Name: {member.first_name}, Age: {member.age}")



# Create a Family object
my_family = Family("Smith")

# Add family members
my_family.born("John", 45)
my_family.born("Jane", 42)
my_family.born("Emma", 17)
my_family.born("Lucas", 20)

# Check if members can go out
my_family.check_majority("Emma")
my_family.check_majority("Lucas")

# Display family information
my_family.family_presentation()