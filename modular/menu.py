MENU = {
    1: {"name": "Classic Cheeseburger", "price": 120.00},
    2: {"name": "Double Crispy Chicken Burger", "price": 165.00},
    3: {"name": "1-pc Fried Chicken w/ Rice", "price": 99.00},
    4: {"name": "Spaghetti Special", "price": 85.00},
    5: {"name": "Large French Fries", "price": 60.00},
    6: {"name": "Iced Tea (16oz)", "price": 35.00},
    7: {"name": "Chocolate Sundae", "price": 45.00}
}


def display_menu():
    print("\n" + "=" * 52)
    print("            WELCOME TO CRAVEBITES FAST FOOD")
    print("               'Taste the Craving Today!'")
    print("=" * 52)
    print(f"{'ID':<5} | {'Item Name':<30} | {'Price (PHP)':>10}")
    print("-" * 52)

    for item_id, details in MENU.items():
        print(
            f"{item_id:<5} | "
            f"{details['name']:<30} | "
            f"₱{details['price']:>9.2f}"
        )

    print("=" * 52)