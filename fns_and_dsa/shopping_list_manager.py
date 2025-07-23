# Display menu function

def display_menu():
    print(f"Shopping List Manager")
    print("Make your choice: ")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# Define main function

def main():
    shopping_list=[]  # List declaration
    while True:
        display_menu()  # call of display_menu function
        choice=input("Enter your choice: ")
        if choice=='1':
            item=input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice=='2':
            remove_item=input("Enter item to remove: ")
            if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
            else: print("Cannot find", remove_item, "in the shopping list\n")
        
        elif choice=='3':
            print(f"\n {shopping_list} \n")
        elif choice=='4':
            print("Goodbye")
            break
        else: print("Invalid choice. please try again")

if __name__== "__main__":
    main()

