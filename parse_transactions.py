import datetime
from typing import Literal, Optional, TypedDict, Union
from constants import CreditCard, Transaction
from utils import parse_date, snakeify_english, to_dict_array


def parse_category_from_description(description: str) -> Optional[str]:
    if "WHOLEFDS" in description:
        return {"category": "Groceries", "sub_category": "Whole Foods"}
    if "netflix.com" in description.lower():
        return {"category": "Entertainment", "sub_category": "Streaming"}

    return None


def parse_category(category: str):
    if "Hardware Supplies" in category:
        return "Home Improvement"

    return None


class BaseRow(TypedDict):
    description: str
    amount: float
    category: str
    date: datetime.date
    type: Union[Literal["payment"], Literal["purchase"]]


def get_base_row(credit_card: CreditCard, row: dict[str, str]) -> BaseRow:
    if credit_card["brand"] == "American Express":
        return {
            "description": row["Description"],
            "category": row["Category"],
            "amount": float(row["Amount"]),
            "date": parse_date(date_str=row["Date"]),
            "type": (
                "payment"
                if "AUTOPAY PAYMENT - THANK YOU" in row["Description"]
                or row["Amount"] < 0
                else "purchase"
            ),
        }
    if credit_card["brand"] == "Discover":
        return {
            "description": row["Description"],
            "category": row["Category"],
            "amount": float(row["Amount"]),
            "date": parse_date(date_str=row["Date"]),
            "type": (
                "payment"
                if "Payments and Credits" in row["Description"] or row["Amount"] < 0
                else "purchase"
            ),
        }
    if credit_card["brand"] == "Chase":
        return {
            "description": row["Description"],
            "category": row["Category"],
            "amount": 0 - float(row["Amount"]),
            "date": parse_date(date_str=row["Date"]),
            "type": (
                "payment"
                if "Payment" in row["Type"]
                or row["Amount"] > 0
                or row["Description"] == "AUTOMATIC PAYMENT - THANK"
                else "purchase"
            ),
        }
    if credit_card["brand"] == "Citi":
        # TODO
        return None
    if credit_card["brand"] == "PNC":
        return {
            "description": row["Description"],
            "category": None,
            "amount": float(row["Amount"]),
            "date": parse_date(date_str=row["Date"]),
            "type": ("payment" if row["Amount"] < 0 else "purchase"),
        }


def parse_transactions(
    *, credit_card: CreditCard, headers: list[str], values: list[list[str]]
) -> list[Transaction]:

    rows = to_dict_array(headers=headers, values=values)
    results = []
    for row in rows:
        base_row = get_base_row(credit_card=credit_card, row=row)

        category_info = parse_category_from_description(row["Description"])

        if not category_info:
            category_info = parse_category(category=row["Category"])

        if not category_info:
            category_info = {"cateogry": "Unknown"}

        result = {
            "description": base_row["description"],
            "category": category_info["category"],
            "sub_category": category_info["sub_category"],
            "date": parse_date(base_row["date"]),
            "amount": base_row["amount"],
            "original_data": row,
        }
        results.append(result)
    return results

    # else:
    #     raise ValueError(f"Unknown credit card brand {credit_card['brand']}")
