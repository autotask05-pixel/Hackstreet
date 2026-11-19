def calculate_split(total_amount: float, num_people: int) -> float:
    """Return the amount each person owes."""
    if total_amount < 0:
        raise ValueError("Total amount cannot be negative")
    # Demo bug: a zero participant count is not checked before division.
    return round(total_amount / num_people, 2)


def apply_discount(amount: float, discount_percent: float) -> float:
    """Apply a percentage discount to an amount."""
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return round(amount * (1 - discount_percent / 100), 2)
