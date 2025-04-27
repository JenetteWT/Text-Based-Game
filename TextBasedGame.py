# Jenette Williams-Thomas
# 04/17/2022

# Function showing instructions
def show_instructions():
    # print a main menu and the commands
    print("Miracle Mall:Getting ready for vacation game!")
    print("Collect 6 items to win the game, or your trip will be cancelled.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: Buy 'item name'\n")


# Main function
def main():
    # Calling function to display instructions
    show_instructions()
    # A dictionary for shopping at Miracle Mall
    # The dictionary links stores to each other
    stores = {"Bank": {"E": "Shoe Store", "item": None},
              "Shoe Store": {"W": "Bank", "N": "Food Court", "S": "Clothing Store",
                             "E": "Beauty Store", "item": "Sandals"},
              "Beauty Store": {"W": "Shoe Store", "N": "Electronics Store", "item": "Perfume"},
              "Electronics Store": {"S": "Beauty Store", "item": "Waterproof phone case"},
              "Clothing Store": {"E": "Swim wear Store", "N": "Shoe Store", "item": "Dress"},
              "Swim wear Store": {"W": "Clothing Store", "item": "Swimsuit"},
              "Food Court": {"S": "Shoe Store", "E": "Pet Store", "item": "Pizza"},
              "Pet Store": {"W": "Food Court", "item": "Miracle sales clerk"},
              }
    # Starting position
    current_store = "Bank"
    # List to store collected items
    inventory = []

    # Loop to simulate moves between stores based on the user input
    while True:
        # If current_store is Pet then loop is broken
        if current_store == "Pet Store":
            print("\nYou are in the", current_store)
            print("A miracle happens!")
            if len(inventory) == 6:
                print("\nCongrats! You have all 6 items and resisted buying a puppy!")
            else:
                print("\nThe Miracle sales clerk shows you a puppy, you fall in love, and buy it! Trip cancelled.")
            break

        # Output current_store
        print("\nYou are in the", current_store)

        # Take user choice to pick up the item or not
        if stores[current_store]['item'] is not None:
            print("You see the perfect", stores[current_store]['item'])
            choice = input("Buy " + stores[current_store]['item'] + "?(Y/N): ").upper()
            # Validate user input
            while choice not in ['Y', 'N']:
                # Output if user puts in invalid choice
                print("Enter a valid option. Y or N")
                choice = input("Buy " + stores[current_store]['item'] + "?(Y/N): ").upper()
            # If user decides to add item to inventory
            if choice == 'Y':
                inventory.append(stores[current_store]['item'])
                stores[current_store]['item'] = None
        else:
            # Output when there is no item available
            print("Already collected item or nothing in this store")

        # Printing inventory
        print("Inventory:", inventory)

        # Taking user input for direction to move
        direction = input("Enter a direction(North == N,South == S,East == E, or West == W): ").title()
        directions = list(stores[current_store].keys())
        directions.remove('item')
        # Validating direction
        while direction not in directions:
            print("Invalid direction from " + current_store + ". Try again")
            direction = input("Direction to move?(go N, go S, go E, go W): ").title()

        # establish the next_store
        next_store = stores[current_store][direction]
        print("You have just moved to", next_store)
        print("------------------------------------------------")

        # Update current_store after move
        current_store = next_store

    # Output end message
    print("\nThanks for playing. Play again soon!")


# Call to main function
main()
