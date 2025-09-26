def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add)
            print(f"'{item_to_add}' has been added to the list.")
        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            else:
                print(f"'{item_to_remove}' was not found in the list.")
        elif choice == '3':
            # Display the shopping list
            print("\nCurrent Shopping List:")
            if shopping_list:
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The list is empty.")
            print("")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
