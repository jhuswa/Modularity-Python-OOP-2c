# main.py
from menu import get_menu, display_menu
from operations import (
    ask_to_order, get_menu_item, get_quantity,
    ask_another_order, calculate_total, calculate_discount
)
from receipts import print_receipt

def main():
    menu = get_menu()
    orders = {}

    display_menu(menu)

    if not ask_to_order():
        print("\nThank you for visiting Jollibee Express!")
        print("Have a great day!")
        return

    ordering = True
    while ordering:
        display_menu(menu)
        selected_item = get_menu_item(menu)
        quantity = get_quantity()

        if selected_item in orders:
            orders[selected_item] += quantity
        else:
            orders[selected_item] = quantity

        print(f"\nAdded {quantity} x {selected_item} to your order.")
        ordering = ask_another_order()

    subtotal = calculate_total(orders, menu)
    discount = calculate_discount(subtotal)
    print_receipt(orders, menu, subtotal, discount)

if __name__ == "__main__":
    main()