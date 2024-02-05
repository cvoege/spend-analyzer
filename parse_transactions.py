import datetime
from pprint import pprint
from typing import Literal, Optional, TypedDict, Union
from constants import CreditCard, Transaction
from utils import parse_date, snakeify_english, to_dict_array


def parse_category_from_description(
    *, category: str, description: str
) -> Optional[str]:
    if "wholefds" in description.lower():
        return {"category": "Groceries", "sub_category": "Whole Foods"}
    elif "netflix.com" in description.lower():
        return {"category": "Entertainment", "sub_category": "Streaming"}
    elif "kagi.com" in description.lower():
        return {"category": "Online Tools", "sub_category": "Search Engines"}
    elif "imax theatre indianapolis" in description.lower():
        return {"category": "Entertainment", "sub_category": "Movie Theatres"}
    elif "old national center_lobby" in description.lower():
        return {"category": "Entertainment", "sub_category": "Concerts"}
    elif "roasting" in description.lower():
        return {"category": "Dining", "sub_category": "Coffee"}
    elif "TARGET        " in description:
        return {"category": "Groceries", "sub_category": "Target"}
    elif "racquet" in description.lower() or "tennis" in description.lower():
        return {"category": "Health & Wellness", "sub_category": "Tennis"}
    elif "FUSEK'S TRUE VALUE" == description:
        return {"category": "Home Improvement", "sub_category": "Hardware Stores"}
    elif "THE HOME DEPOT" in description:
        return {"category": "Home Improvement", "sub_category": "Hardware Stores"}
    elif "SOUTHWES    " in description and (category in {"Travel", "Unknown"}):
        return {"category": "Travel", "sub_category": "Flights"}
    elif "DELTA AIR" in description and (category in {"Travel", "Unknown"}):
        return {"category": "Travel", "sub_category": "Flights"}
    elif "FRONTIER" in description and (category in {"Travel", "Unknown"}):
        return {"category": "Travel", "sub_category": "Flights"}
    elif "MISTER SPARKY-INDY" == description:
        return {"category": "Home Improvement", "sub_category": "Electricians"}
    elif "inn" in description.lower() and (category in {"Travel", "Unknown"}):
        return {"category": "Travel", "sub_category": "Hotels"}
    elif "hotels" in description.lower() and (category in {"Travel", "Unknown"}):
        return {"category": "Travel", "sub_category": "Hotels"}
    elif "ikea" in description.lower() and (
        category in {"Home", "Home Improvement", "Unknown"}
    ):
        return {"category": "Home Improvement", "sub_category": "Furniture Stores"}
    elif "heating" in description.lower() and (
        category in {"Home", "Home Improvement", "Unknown"}
    ):
        return {"category": "Home Improvement", "sub_category": "HVAC"}
    elif "control tech" in description.lower() and (
        category in {"Home", "Home Improvement", "Unknown"}
    ):
        return {"category": "Home Improvement", "sub_category": "HVAC"}
    elif "ben franklin" in description.lower() and (
        category in {"Home", "Home Improvement", "Unknown"}
    ):
        return {"category": "Home Improvement", "sub_category": "Plumbing"}
    elif "LS SILVER IN THE CITY" in description:
        return {"category": "Shopping", "sub_category": "Gift Shops"}
    elif "LS GRAY GOAT BICYCLE" in description:
        return {"category": "Shopping", "sub_category": "Bike Shops"}
    elif "CVS/PHARMACY" in description:
        return {"category": "Drug Stores"}
    elif "FREEWHEELIN COMMUNITY BI" == description:
        return {"category": "Shopping", "sub_category": "Bike Shops"}
    elif "MUSEUM" == description:
        return {"category": "Education", "sub_category": "Museums"}
    elif "GENTSPA AT THE HILTON" == description:
        return {"category": "Personal", "sub_category": "Hair"}
    elif "NYTimes" in description:
        return {"category": "Entertainment", "sub_category": "Newspapers"}
    elif "Prime Video" in description:
        return {"category": "Entertainment", "sub_category": "Streaming"}
    elif "AMZN Mktp" in description:
        return {"category": "Shopping", "sub_category": "Amazon"}
    elif "Amazon Prime*" in description:
        return {"category": "Shopping", "sub_category": "Amazon"}
    elif "TURBOTAX" in description:
        return {"category": "Online Tools", "sub_category": "Tax Software"}
    elif "USTA LEAGUES" in description:
        return {"category": "Health & Wellness", "sub_category": "Tennis"}
    elif "USTA MEMBERSHIP" in description:
        return {"category": "Health & Wellness", "sub_category": "Tennis"}
    elif "nintendo" in description.lower():
        return {"category": "Entertainment", "sub_category": "Video Games"}
    elif "nintendo" in description.lower():
        return {"category": "Entertainment", "sub_category": "Video Games"}
    elif (
        "steam purchase" in description.lower()
        or "valve bellevue wa" in description.lower()
    ):
        return {"category": "Entertainment", "sub_category": "Video Games"}
    elif "gaijin games" in description.lower():
        return {"category": "Entertainment", "sub_category": "Video Games"}
    elif "Oculus" == description:
        return {"category": "Entertainment", "sub_category": "Video Games"}
    elif "top golf" in description.lower():
        return {"category": "Entertainment"}
    elif "target.com" in description.lower():
        return {"category": "Shopping", "sub_category": "Online Retailers"}
    elif "walmart.com" in description.lower():
        return {"category": "Shopping", "sub_category": "Online Retailers"}
    elif "name-cheap.com" in description.lower():
        return {"category": "Online Tools", "sub_category": "Domain Hosting"}
    elif "foreign transaction fee" in description.lower():
        return {"category": "Fees", "sub_category": "Foreign Transaction Fees"}
    elif "uber" in description.lower() and "trip" in description.lower():
        return {"category": "Travel", "sub_category": "Ride Sharing"}
    elif "www.massaveanimalclini" in description.lower():
        return {"category": "Veterinary"}
    elif "mountain" in description.lower():  # Rough skiing check
        return {"category": "Entertainment"}

    return None


def parse_category(*, category: str, description: str):
    category_info = parse_category_from_description(
        category=category, description=description
    )
    if category_info:
        return category_info

    if "Hardware Supplies" in category:
        return {"category": "Home Improvement"}
    elif category in {"Groceries", "Merchandise & Supplies-Groceries"}:
        return {"category": "Groceries", "sub_category": "Grocery Stores"}
    elif category in {"Entertainment", "Travel/ Entertainment"}:
        return {"category": "Entertainment"}
    elif category == "Gas":
        return {"category": "Gas"}
    elif category == "Health & Wellness":
        return {"category": "Health & Wellness"}
    elif category == "Bills & Utilities":
        return {"category": "Utilities"}
    elif category in {"Home", "Home Improvement"}:
        return {"category": "Home Improvement"}
    elif category == "Travel":
        return {"category": "Travel"}
    elif category in ("Food & Drink", "Restaurants", "Dining"):
        return {"category": "Dining"}
    elif category in ("Shopping", "Merchandise"):
        return {"category": "Shopping"}
    elif category == "Personal":
        return {"category": "Personal"}
    elif category == "Gifts & Donations":
        return {"category": "Donations"}
    elif category == "Supermarkets":
        return {"category": "Groceries", "sub_category": "Supermarkets"}
    elif category == "Automotive":
        return {"category": "Automotive"}
    elif category in ("Services", "Professional Services"):
        return {"category": "Services"}

    return None


class BaseRow(TypedDict):
    description: str
    amount: float
    category: str
    date: datetime.date
    type: Union[Literal["payment"], Literal["purchase"]]


def get_base_row(credit_card: CreditCard, row: dict[str, str]) -> BaseRow:
    amount = float(row["Amount"].replace("$", ""))
    if credit_card["brand"] == "American Express":
        return {
            "description": row["Description"],
            "category": row["Category"],
            "amount": amount,
            "date": parse_date(date_str=row["Date"]),
            "type": (
                "payment"
                if "AUTOPAY PAYMENT - THANK YOU" in row["Description"] or amount < 0
                else "purchase"
            ),
        }
    elif credit_card["brand"] == "Discover":
        return {
            "description": row["Description"],
            "category": row["Category"],
            "amount": amount,
            "date": parse_date(date_str=row["Trans. Date"]),
            "type": (
                "payment"
                if "Payments and Credits" in row["Description"] or amount < 0
                else "purchase"
            ),
        }
    elif credit_card["brand"] == "Chase":
        return {
            "description": row["Description"],
            "category": row["Category"],
            "amount": 0 - amount,
            "date": parse_date(date_str=row["Transaction Date"]),
            "type": (
                "payment"
                if "Payment" in row["Type"]
                or amount > 0
                or row["Description"] == "AUTOMATIC PAYMENT - THANK"
                else "purchase"
            ),
        }
    elif credit_card["brand"] == "Citi":
        # TODO
        return None
    elif credit_card["brand"] == "PNC":
        return {
            "description": row["Description"],
            "category": "Unknown",
            "amount": amount,
            "date": parse_date(date_str=row["Date"]),
            "type": ("payment" if amount < 0 else "purchase"),
        }
    else:
        raise ValueError(f"Unknown credit card brand {credit_card['brand']}")


def parse_transactions(
    *, credit_card: CreditCard, headers: list[str], values: list[list[str]]
) -> list[Transaction]:
    rows = to_dict_array(headers=headers, values=values)
    results = []
    for row in rows:
        base_row = get_base_row(credit_card=credit_card, row=row)
        original_category = base_row["category"]

        if base_row["type"] == "payment":
            continue

        category_info = parse_category(
            description=base_row["description"], category=original_category
        )

        if not category_info:
            category_info = {"category": "Unknown"}

        result = {
            "description": base_row["description"],
            "category": category_info["category"],
            "sub_category": category_info.get("sub_category", "Unknown"),
            "original_category": original_category,
            "date": base_row["date"],
            "amount": base_row["amount"],
            "credit_card_name": credit_card["name"],
            "original_data": row,
        }
        results.append(result)
    return results
