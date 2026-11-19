from calculator import apply_discount, calculate_split
from utils.parser import parse_split_request


def process_bill(payload: dict) -> dict:
    total, people = parse_split_request(payload)
    discounted_total = apply_discount(total, payload.get("discount", 0.0))
    per_person = calculate_split(discounted_total, people)
    return {
        "discounted_total": discounted_total,
        "people": people,
        "per_person": per_person,
    }


if __name__ == "__main__":
    print(process_bill({"total": 120.0, "people": 0, "discount": 10.0}))
