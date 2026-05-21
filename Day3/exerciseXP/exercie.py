
#exercice1 

# Create the Cat class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


#  Create three cat instances
cat1 = Cat("Mimi", 2)
cat2 = Cat("Tiger", 5)
cat3 = Cat("Bella", 3)


# : Function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1

    if cat2.age > oldest.age:
        oldest = cat2

    if cat3.age > oldest.age:
        oldest = cat3

    return oldest



oldest_cat = find_oldest_cat(cat1, cat2, cat3)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


#exercice2

# Create the Dog class
class Dog:
    def __init__(self, name, height):
        # Initialize dog attributes
        self.name = name
        self.height = height

    # Method for barking
    def bark(self):
        print(f"{self.name} goes woof!")

    # Method for jumping
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


# Step 2: Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Buddy", 35)


# Step 3: Print dog details and call methods
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print()

print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()


# Step 4: Compare dog sizes
if davids_dog.height > sarahs_dog.height:
    print(f"\n{davids_dog.name} is taller than {sarahs_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"\n{sarahs_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"\n{davids_dog.name} and {sarahs_dog.name} are the same height.")
    
    
    
    
#exercise3    

# Create the Song class
class Song:
    def __init__(self, lyrics):
        # Initialize the lyrics attribute
        self.lyrics = lyrics

    # Method to print the song lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# Create a Song object
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Call the method to print the lyrics
stairway.sing_me_a_song()



#exercise4


# Create the Zoo class
class Zoo:
    def __init__(self, zoo_name):
        # Initialize zoo name and animals list
        self.zoo_name = zoo_name
        self.animals = []
        self.grouped_animals = {}

    # Method to add one or multiple animals
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    # Method to display all animals
    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    # Method to remove an animal
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    # Method to sort and group animals
    def sort_animals(self):
        # Sort animals alphabetically
        sorted_animals = sorted(self.animals)

        # Create dictionary for grouped animals
        self.grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0]

            # Create a new group if letter does not exist
            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = []

            # Add animal to the correct group
            self.grouped_animals[first_letter].append(animal)

    # Method to display grouped animals
    def get_groups(self):
        print("Grouped animals:")

        for letter, animals in self.grouped_animals.items():
            print(f"{letter}: {animals}")


# Step 2: Create a Zoo object
brooklyn_safari = Zoo("Brooklyn Safari")


# Step 3: Use the Zoo methods
brooklyn_safari.add_animal(
    "Giraffe",
    "Bear",
    "Baboon",
    "Lion",
    "Zebra",
    "Cat",
    "Cougar"
)

# Display animals
brooklyn_safari.get_animals()

print()

# Sell an animal
brooklyn_safari.sell_animal("Bear")

print()

# Display animals after selling
brooklyn_safari.get_animals()

print()

# Sort and group animals
brooklyn_safari.sort_animals()

# Display grouped animals
brooklyn_safari.get_groups()

