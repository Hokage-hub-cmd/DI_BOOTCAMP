#exercise 1 

print("Hello world\nHello world\nHello world\nHello world")

#exercise 2 

print((99**3)*8)

#exercise 3

15 < 8 #False 


5 < 3 #False
 
3 == 3 #True

3 == "3" #False

"3" > 3 #True

"Hello" == "hello" #False

#exercise 4

# Your computer brand

# Create a variable to store the computer brand
computer_brand = "HP"

# Display the requested sentence
print(f"I have a {computer_brand} computer.")

#exercise 5

#Your information

# create variables to store your name, age and shoe size
name = "Kage hopper kuhlmann"
age = 60
shoe_size = 42

# Créer une phrase avec toutes les infos
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."

# Afficher la phrase
print(info)



#exercise 6

# Create two variables a and b, and assign them any values you want.
a = 10
b = 5

# Condition
if a > b:
    print("Hello World")
    
#exercise 7
    
# ask the user for a number and determine if it is even or odd     
number = int(input("Enter a number: "))

# Verify if the number is even or odd
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
       
#exercise 8

 
# your name
my_name = "Kage"

# ask the user for their name
user_name = input("What is your name? ")

# Verify if the user's name is the same as yours and print a message accordingly
if user_name == my_name:
    print("Wow! We have the same name ")
else:
    print("i'm so glad to see you  my friend " + user_name + "!")
    
    
#exercise 9          

# Ask the user for their height in centimeters
height = int(input("Enter your height in cm: "))

# Check if the user is tall enough
if height > 145:
    print("You are tall enough to ride the roller coaster!")
else:
    print("You need to grow some more to ride.")