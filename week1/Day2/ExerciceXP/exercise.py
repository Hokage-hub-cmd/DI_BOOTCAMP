#exercise 1 
#the values of the dictionary are the same as the keys but in lower case
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# creating a dictionary using zip function 

mon_dictionnaire = dict(zip(keys, values))

print(mon_dictionnaire)


#exercise 2


# data for the family members and their ages

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

cout_total = 0


# run through the family members and calculate the ticket price based on their age

for nom, age in family.items():
   
    
    if age < 3:
        prix_billet = 0
    elif 3 <= age <= 12:
        prix_billet = 10
    else:
        prix_billet = 15

    # print the ticket price for each family member
    print(f"Billet pour {nom.capitalize()} ({age} ans) : {prix_billet} $")

    
    cout_total += prix_billet

print("-" * 30)
print(f"Coût total pour la famille : {cout_total} $")


#prime 

# Initialize an empty dictionary for the family and the total cost
family = {}
total_cost = 0

print("--- Family Configuration ---")

# 1. Loop to request information from the user
while True:
    name = input("Entrer le nom du membre (ou taper 'fin' pour arrêter): ").strip()
    
    # If the user types 'fin', stop the input loop
    if name.lower() == 'fin':
        break
        
    # Safety check to ensure the age entered is a valid integer
    try:
        age = int(input(f"Entrer l'âge de {name}: "))
        family[name] = age  # Add the member to the dictionary
    except ValueError:
        print("Please enter a valid age as a number.")

print("\n--- Cinemax Billing ---")

# 2. Calculate the ticket pricing for the custom family
for name, age in family.items():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
        
    print(f"Ticket for {name.capitalize()} ({age} years old): {ticket_price} $")
    total_cost += ticket_price

print("-" * 30)
print(f"Final total cost: {total_cost} $")



#Exercice3 


brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# 2. Change the value of number_stores to 2
brand["number_stores"] = 2

# 3. Print a sentence describing Zara's clients
clients = ", ".join(brand["type_of_clothes"])
print(f"Zara offers clothes for: {clients}.")

# 4. Add the key country_creation with the value Spain
brand["country_creation"] = "Spain"

# 5. Check if international_competitors exists and add Desigual
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6. Remove the key creation_date
brand.pop("creation_date")

# 7. Print the last element in international_competitors
last_competitor = brand["international_competitors"][-1]
print(f"The last competitor added is: {last_competitor}")

# 8. Print the major colors in the US
us_colors = ", ".join(brand["major_color"]["US"])
print(f"The major colors in the US are: {us_colors}")

# 9. Display the number of keys in the dictionary
keys_count = len(brand)
print(f"The dictionary contains {keys_count} keys.")

# 10. Print all the keys in the dictionary
print("List of keys:", list(brand.keys()))


# --- BONUS (PRIME) PART ---

# Create the second dictionary requested
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# Merge (update) the original 'brand' dictionary with the new one
brand.update(more_on_zara)

# Display the final merged result
print("\nBrand dictionary after merging with the bonus:")
print(brand)



#exercise4

# Step 1 & 2: Define the function with a default parameter value for country

def describe_city(city, country="Unknown"):
    # Print the formatted sentence combining city and country
    print(f"{city} is in {country}.")

# Step 3: Call the function with different combinations
# Call with both arguments provided
describe_city("Reykjavik", "Iceland")

# Call with only the city argument (uses the default country value)
describe_city("Paris")

# Call with another example
describe_city("Tokyo", "Japan")

#exercice5


import random

# Step 2: Define the function with a single parameter
def compare_numbers(user_number):
   
    random_number = random.randint(1, 100)
    
    
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")


compare_numbers(50)



#exercise6 

def make_shirt(size="large", text="I love Python"):
    """Prints a summary message of the shirt size and text."""
    
    print(f"The size of the shirt is {size} and the text is {text}.")


make_shirt()

make_shirt(size="medium")

make_shirt("small", "Custom message")


make_shirt(text="Hello World!", size="extra-large")


#exercise7 

import random

# Step 4 & 5: Modified function to accept a season and return a float temperature
def get_random_temp(season):
    # Set temperature ranges based on the determined season
    if season == "winter":
        return random.uniform(-10.0, 5.0)
    elif season == "spring":
        return random.uniform(6.0, 20.0)
    elif season == "summer":
        return random.uniform(21.0, 40.0)
    elif season == "autumn":
        return random.uniform(5.0, 15.0)
    else:
        # Step 1 fallback: Default general range from -10 to 40
        return random.uniform(-10.0, 40.0)

# Step 2: Define the main function
def main():
    print("--- Season and Temperature Advisor ---")
    
    # Step 5 Bonus: Ask the user for a month number
    try:
        month = int(input("Enter a month number (1-12): "))
        
        # Determine the season using if/elif conditions based on the month
        if not 1 <= month <= 12:
            print("Invalid month. Defaulting to general temperature range.")
            season = "unknown"
        elif month in [12, 1, 2]:
            season = "winter"
        elif month in [3, 4, 5]:
            season = "spring"
        elif month in [6, 7, 8]:
            season = "summer"
        else:
            season = "autumn"
            
    except ValueError:
        print("Invalid input. Defaulting to general temperature range.")
        season = "unknown"

    # Step 2: Call get_random_temp and round the float to 1 decimal place
    temperature = round(get_random_temp(season), 1)
    
    # Print the friendly message
    print(f"\nThe temperature right now is {temperature} degrees Celsius.")
    
    # Step 3: Provide advice based on temperature thresholds
    if temperature < 0:
        print("Brrr, that's freezing! Wear extra layers today.")
    elif 0 <= temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 <= temperature < 24:
        print("Beautiful weather.")
    elif 24 <= temperature < 32:
        print("It's getting warm, remember to stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()


#exercise8

# Initialize base price, topping price, and an empty list for toppings
base_price = 10.0
topping_price = 2.5
toppings = []

print("--- Welcome to Pizza Builder ---")

# Loop to ask the user for pizza toppings one by one
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ").strip()
    
    # Stop the loop if the user types 'quit'
    if topping.lower() == 'quit':
        break
    
    # Add the topping to the list and print confirmation
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

# Calculate the final total price
total_price = base_price + (len(toppings) * topping_price)

# Display final pizza toppings and total price
print("\n--- Your Order Summary ---")
if toppings:
    print("Your toppings:")
    for item in toppings:
        print(f"- {item}")
else:
    print("Your pizza has no extra toppings (Plain Cheese).")

print("-" * 25)
print(f"Total price: {total_price:.2f} $")

