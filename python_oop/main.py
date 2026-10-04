import datetime


class CraveBitesSystem:

    def __init__(self):
        self.menu = {
            1: {"name": "Classic Cheeseburger", "price": 120.00},
            2: {"name": "Double Crispy Chicken Burger", "price": 165.00},
            3: {"name": "1-pc Fried Chicken w/ Rice", "price": 99.00},
            4: {"name": "Spaghetti Special", "price": 85.00},
            5: {"name": "Large French Fries", "price": 60.00},
            6: {"name": "Iced Tea (16oz)", "price": 35.00},
            7: {"name": "Chocolate Sundae", "price": 45.00}
        }

        self.order_list = []

    def display_menu(self):

        print("\n" + "=" * 52)
        print("            WELCOME TO CRAVEBITES FAST FOOD")
        print("               'Taste the Craving Today!'")
        print("=" * 52)
        print(f"{'ID':<5} | {'Item Name':<30} | {'Price (PHP)':>10}")
        print("-" * 52)

        for item_id, details in self.menu.items():
            print(
                f"{item_id:<5} | "
                f"{details['name']:<30} | "
                f"₱{details['price']:>9.2f}"
            )

        print("=" * 52)

    def get_valid_integer(self, prompt):

        while True:
            try:
                value = int(input(prompt))

                if value > 0:
                    return value

                print("   [!] Error: Please enter a number greater than 0.")

            except ValueError:
                print("   [!] Error: Invalid input. Please enter a valid number.")

    def take_order(self):

        while True:
            choice = input(
                "\nWould you like to place an order? (yes/no): "
            ).strip().lower()

            if choice in ["yes", "y"]:
                break

            elif choice in ["no", "n"]:
                print(
                    "\nThank you for visiting CraveBites! "
                    "Have a great day!"
                )
                return False

            else:
                print("   [!] Error: Please enter 'yes' or 'no'.")

        ordering = True

        while ordering:

            print("\n--- ADD ITEM TO ORDER ---")

            item_id = self.get_valid_integer("Enter Item ID: ")

            if item_id not in self.menu:
                print(
                    "   [!] Error: Item ID does not exist "
                    "in the menu."
                )
                continue

            quantity = self.get_valid_integer(
                f"Enter quantity for "
                f"'{self.menu[item_id]['name']}': "
            )

            self.order_list.append({
                "name": self.menu[item_id]["name"],
                "price": self.menu[item_id]["price"],
                "quantity": quantity,
                "item_total": self.menu[item_id]["price"] * quantity
            })

            print(
                f"   [✓] Added {quantity}x "
                f"{self.menu[item_id]['name']} to your cart."
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
                    print(
                        "   [!] Error: Please enter 'yes' or 'no'."
                    )

        return True

    def calculate_totals(self):

        subtotal = 0.0

        for item in self.order_list:
            subtotal += item["item_total"]

        discount_rate = 0.10 if subtotal >= 500.00 else 0.0
        discount_amount = subtotal * discount_rate
        grand_total = subtotal - discount_amount

        return subtotal, discount_amount, grand_total

    def print_receipt(self, subtotal, discount_amount, grand_total):

        now = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print("\n" + "*" * 52)
        print("                 CRAVEBITES FAST FOOD")
        print("             123 Main Street, Central Hub")
        print("                  TEL: (032) 888-9999")
        print("*" * 52)

        print(f" Date/Time: {now}")
        print(
            f" Receipt No: "
            f"CB-{datetime.datetime.now().strftime('%M%S')}"
        )

        print("-" * 52)
        print(
            f"{'Qty':<4} "
            f"{'Item Description':<25} "
            f"{'Price':>9} "
            f"{'Total':>10}"
        )
        print("-" * 52)

        for item in self.order_list:
            print(
                f"{item['quantity']:<4} "
                f"{item['name']:<25} "
                f"₱{item['price']:>8.2f} "
                f"₱{item['item_total']:>9.2f}"
            )

        print("-" * 52)
        print(f"{'Subtotal:':<40} ₱{subtotal:>9.2f}")

        if discount_amount > 0:
            print(
                f"{'Discount (10% Promo >= ₱500):':<40}"
                f"-₱{discount_amount:>9.2f}"
            )

        print(
            f"{'GRAND TOTAL:':<40} "
            f"₱{grand_total:>9.2f}"
        )

        print("=" * 52)
        print("          Thank you for dining at CraveBites!")
        print("               Please come again soon!")
        print("*" * 52)

    def run(self):

        self.display_menu()

        if self.take_order():

            subtotal, discount, grand_total = (
                self.calculate_totals()
            )

            self.print_receipt(
                subtotal,
                discount,
                grand_total
            )