def process_payment(amount):
    if amount <= 0:
        return "Invalid amount"

    return "Payment successful"


def checkout(user, amount):
    payment_status = process_payment(amount)

    if payment_status == "Payment successful":
        return f"Order confirmed for {user}"
    else:
        return "Payment failed"
