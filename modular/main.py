from menu import display_menu
from order import take_order
from calculation import calculate_totals
from receipt import print_receipt


def main():

    display_menu()

    user_orders = take_order()

    if user_orders:
        subtotal, discount, grand_total = calculate_totals(user_orders)

        print_receipt(
            user_orders,
            subtotal,
            discount,
            grand_total
        )


if __name__ == "__main__":
    main()