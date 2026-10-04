import datetime


def print_receipt(order_list, subtotal, discount_amount, grand_total):

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

    for item in order_list:
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

    print(f"{'GRAND TOTAL:':<40} ₱{grand_total:>9.2f}")

    print("=" * 52)
    print("          Thank you for dining at CraveBites!")
    print("               Please come again soon!")
    print("*" * 52)
