# receipts.py

def print_receipt(orders, menu, subtotal, discount):
    total = subtotal - discount

    print("\n")
    print("=" * 55)
    print("                  JOLLIBEE EXPRESS")
    print("                  OFFICIAL RECEIPT")
    print("=" * 55)

    print(f"{'ITEM':<22}{'QTY':>5}{'PRICE':>12}{'TOTAL':>12}")
    print("-" * 55)

    for item, quantity in orders.items():
        price = menu[item]
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