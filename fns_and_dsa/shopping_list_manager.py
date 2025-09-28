shopping_list = []
def DisplayMenu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")
        
    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")
            
    elif choice == '3':
        print("Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
            
    elif choice == '4':
        print("Exiting Shopping List Manager.")
        break
        
    else:
        print("Invalid choice. Please try again.")
        
    print() 