# operations.py

def ask_to_order():
    while True:
        answer = input("\nWould you like to order? (yes/no): ").lower().strip()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter yes or no.")

def get_menu_item(menu):
    while True:
        item_number = input("\nEnter the menu item number: ").strip()
        if item_number.isdigit():
            item_number = int(item_number)
            menu_items = list(menu.keys())
            if 1 <= item_number <= len(menu_items):
                return menu_items[item_number - 1]
        print("Invalid menu item. Please choose a number from the menu.")

def get_quantity():
    while True:
        quantity = input("Enter quantity: ").strip()
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity > 0:
                return quantity
        print("Invalid quantity. Please enter a number greater than 0.")

def ask_another_order():
    while True:
        answer = input("\nWould you like to order another item? (yes/no): ").lower().strip()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter yes or no.")

def calculate_total(orders, menu):
    subtotal = 0
    for item, quantity in orders.items():
        subtotal += menu[item] * quantity
    return subtotal

def calculate_discount(subtotal):
    if subtotal >= 500:
        return subtotal * 0.10
    return 0