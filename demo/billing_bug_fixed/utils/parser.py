"""Helpers for reading a bill request."""


def parse_split_request(payload: dict) -> tuple[float, int]:
    total = payload.get("total", 0.0)
    people = payload.get("people", 0)
    return float(total), int(people)
