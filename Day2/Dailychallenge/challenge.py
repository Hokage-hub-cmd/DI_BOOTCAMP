#challenge 1


user_word = input("Please enter a word: ").strip()


letter_indices = {}

# Loop through the word keeping track of both the index and the character
for index, char in enumerate(user_word):
    # Check if the character is already a key in the dictionary
    if char in letter_indices:
        # If it is, append the current index to the existing list
        letter_indices[char].append(index)
    else:
        # If it is not, create a new key with the index inside a list
        letter_indices[char] = [index]


print(letter_indices)


#challenge 2

def buy_items(items_purchase, wallet):
    # Clean the wallet string to extract the integer value
    wallet_clean = int(wallet.replace("$", "").replace(",", ""))
    basket = []

    # Loop through items in order of priority (dictionary order)
    for item, price_str in items_purchase.items():
        # Clean the price string to extract the integer value
        price_clean = int(price_str.replace("$", "").replace(",", ""))

        # Check if we can afford the item
        if wallet_clean >= price_clean:
            basket.append(item)  # Add item to basket
            wallet_clean -= price_clean  # Deduct price from wallet

    # Check if the basket is empty
    if not basket:
        return "Nothing"
    else:
        # Return the basket sorted alphabetically
        return sorted(basket)


# --- TEST CASES FROM THE EXERCISE ---

# Test Case 1
items_1 = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet_1 = "$300"
print(f"Result 1: {buy_items(items_1, wallet_1)}")

# Test Case 2
items_2 = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2",
}
wallet_2 = "$100"
print(f"Result 2: {buy_items(items_2, wallet_2)}")

# Test Case 3
items_3 = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200",
}
wallet_3 = "$1"
print(f"Result 3: {buy_items(items_3, wallet_3)}")


