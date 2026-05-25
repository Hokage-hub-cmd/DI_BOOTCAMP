#Challenge: Create a Farm class with methods to add animals, display information, and list animal types.

# Create the Farm class
class Farm:
    def __init__(self, farm_name):
        # Initialize farm name and animals dictionary
        self.name = farm_name
        self.animals = {}

    # Method to add one or multiple animals
    def add_animal(self, **kwargs):
        for animal_type, count in kwargs.items():

            # If animal already exists, increase the count
            if animal_type in self.animals:
                self.animals[animal_type] += count

            # Otherwise, add the animal to the dictionary
            else:
                self.animals[animal_type] = count

    # Method to display full farm information
    def get_info(self):
        info = f"{self.name}'s farm\n\n"

        # Add each animal and its count
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"

        info += "\nE-I-E-I-0!"

        return info

    # Method to return sorted animal types
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Method to return short farm information
    def get_short_info(self):
        animal_list = []

        # Add "s" for plural animals
        for animal in self.get_animal_types():

            if self.animals[animal] > 1:
                animal_list.append(animal + "s")
            else:
                animal_list.append(animal)

        # Format the animal list correctly
        if len(animal_list) > 1:
            animals_text = ", ".join(animal_list[:-1])
            animals_text += f" and {animal_list[-1]}"
        else:
            animals_text = animal_list[0]

        return f"{self.name}'s farm has {animals_text}."


# Test the code
macdonald = Farm("McDonald")

# Add animals
macdonald.add_animal(cow=5, sheep=2, goat=12)

# Display full information
print(macdonald.get_info())

print()

# Display sorted animal types
print(macdonald.get_animal_types())

print()

# Display short information
print(macdonald.get_short_info())