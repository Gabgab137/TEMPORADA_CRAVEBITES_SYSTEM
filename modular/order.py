from menu import MENU


def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value
            else:
                print("   [!] Error: Please enter a number greater than 0.")

        except ValueError:
            print("   [!] Error: Invalid input. Please enter a valid number.")


def take_order():
    order_list = []

    while True:
        choice = input(
            "\nWould you like to place an order? (yes/no): "
        ).strip().lower()

        if choice in ["yes", "y"]:
            break

        elif choice in ["no", "n"]:
            print("\nThank you for visiting CraveBites! Have a great day!")
            return None

        else:
            print("   [!] Error: Please enter 'yes' or 'no'.")

    ordering = True

    while ordering:
        print("\n--- ADD ITEM TO ORDER ---")

        item_id = get_valid_integer("Enter Item ID: ")

        if item_id not in MENU:
            print("   [!] Error: Item ID does not exist in the menu.")
            continue

        quantity = get_valid_integer(
            f"Enter quantity for '{MENU[item_id]['name']}': "
        )

        order_list.append({
            "name": MENU[item_id]["name"],
            "price": MENU[item_id]["price"],
            "quantity": quantity,
            "item_total": MENU[item_id]["price"] * quantity
        })

        print(
            f"   [✓] Added {quantity}x "
            f"{MENU[item_id]['name']} to your cart."
        )

        while True:
            another = input(
                "\nWould you like to order another item? (yes/no): "
            ).strip().lower()

            if another in ["yes", "y"]:
                break

            elif another in ["no", "n"]:
                ordering = False
                break

            else:
                print("   [!] Error: Please enter 'yes' or 'no'.")

    return order_list