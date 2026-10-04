def calculate_totals(order_list):
    subtotal = 0.0

    for item in order_list:
        subtotal += item["item_total"]

    discount_rate = 0.10 if subtotal >= 500.00 else 0.0
    discount_amount = subtotal * discount_rate
    grand_total = subtotal - discount_amount

    return subtotal, discount_amount, grand_total
