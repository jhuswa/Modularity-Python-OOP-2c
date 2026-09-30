# restaurant.py

class JollibeeExpress:
    def __init__(self):
        self.menu = {
            "1. Chickenjoy with Rice": 99.00,
            "2. Jolly Spaghetti": 75.00,
            "3. Yumburger": 45.00,
            "4. Burger Steak": 85.00,
            "5. Fries": 55.00,
            "6. Peach Mango Pie": 45.00,
            "7. Coke": 40.00,
            "8. Iced Tea": 45.00
        }
        self.orders = {}

    def display_menu(self):
        print("\n" + "=" * 45)
        print("             JOLLIBEE EXPRESS")
        print("                FULL MENU")
        print("=" * 45)
        for item, price in self.menu.items():
            print(f"{item:<30} ₱{price:>8.2f}")
        print("=" * 45)

    def ask_to_order(self):
        while True:
            answer = input("\nWould you like to order? (yes/no): ").lower().strip()
            if answer in ["yes", "y"]:
                return True
            elif answer in ["no", "n"]:
                return False
            else:
                print("Invalid input. Please enter yes or no.")

    def get_menu_item(self):
        while True:
            item_number = input("\nEnter the menu item number: ").strip()
            if item_number.isdigit():
                item_number = int(item_number)
                menu_items = list(self.menu.keys())
                if 1 <= item_number <= len(menu_items):
                    return menu_items[item_number - 1]
            print("Invalid menu item. Please choose a number from the menu.")

    def get_quantity(self):
        while True:
            quantity = input("Enter quantity: ").strip()
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0:
                    return quantity
            print("Invalid quantity. Please enter a number greater than 0.")

    def ask_another_order(self):
        while True:
            answer = input("\nWould you like to order another item? (yes/no): ").lower().strip()
            if answer in ["yes", "y"]:
                return True
            elif answer in ["no", "n"]:
                return False
            else:
                print("Invalid input. Please enter yes or no.")

    def calculate_total(self):
        subtotal = 0
        for item, quantity in self.orders.items():
            subtotal += self.menu[item] * quantity
        return subtotal

    def calculate_discount(self, subtotal):
        if subtotal >= 500:
            return subtotal * 0.10
        return 0

    def print_receipt(self):
        subtotal = self.calculate_total()
        discount = self.calculate_discount(subtotal)
        total = subtotal - discount

        print("\n")
        print("=" * 55)
        print("                  JOLLIBEE EXPRESS")
        print("                  OFFICIAL RECEIPT")
        print("=" * 55)

        print(f"{'ITEM':<22}{'QTY':>5}{'PRICE':>12}{'TOTAL':>12}")
        print("-" * 55)

        for item, quantity in self.orders.items():
            price = self.menu[item]
            item_total = price * quantity
            print(f"{item:<22}{quantity:>5}₱{price:>11.2f}₱{item_total:>11.2f}")

        print("-" * 55)
        print(f"{'SUBTOTAL':<42}₱{subtotal:>11.2f}")
        print(f"{'DISCOUNT':<42}₱{discount:>11.2f}")
        print("=" * 55)
        print(f"{'TOTAL AMOUNT':<42}₱{total:>11.2f}")
        print("=" * 55)
        print("        Thank you for ordering with us!")
        print("                Please come again!")
        print("=" * 55)

    def run(self):
        self.display_menu()

        if not self.ask_to_order():
            print("\nThank you for visiting Jollibee Express!")
            print("Have a great day!")
            return

        ordering = True
        while ordering:
            self.display_menu()
            selected_item = self.get_menu_item()
            quantity = self.get_quantity()

            if selected_item in self.orders:
                self.orders[selected_item] += quantity
            else:
                self.orders[selected_item] = quantity

            print(f"\nAdded {quantity} x {selected_item} to your order.")
            ordering = self.ask_another_order()

        self.print_receipt()