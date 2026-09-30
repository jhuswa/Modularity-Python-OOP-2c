# menu.py

def get_menu():
    return {
        "1. Chickenjoy with Rice": 99.00,
        "2. Jolly Spaghetti": 75.00,
        "3. Yumburger": 45.00,
        "4. Burger Steak": 85.00,
        "5. Fries": 55.00,
        "6. Peach Mango Pie": 45.00,
        "7. Coke": 40.00,
        "8. Iced Tea": 45.00
    }

def display_menu(menu):
    print("\n" + "=" * 45)
    print("             JOLLIBEE EXPRESS")
    print("                FULL MENU")
    print("=" * 45)
    for item, price in menu.items():
        print(f"{item:<30} ₱{price:>8.2f}")
    print("=" * 45)