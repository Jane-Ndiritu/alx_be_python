shopping_list = []

def display_menu():
    print(f"\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(lst):
    item = input("Enter the item to add: ")
    lst.append(item)
    print(f"✅ {item} has been added to your shopping list.")

def remove_item(lst):
    item = input("Enter the item to remove: ")
    if item in lst:
        lst.remove(item)
        print(f"❌ {item} has been removed from your shopping list.")
    else:
        print(f"⚠️ {item} is not in your shopping list.")

def view_list(lst):
    if lst:
        print("\n🛒 Your Shopping List:")
        for i, item in enumerate(lst, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("👋 Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1–4.")

if __name__ == "__main__":
    main()
