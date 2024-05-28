import datetime
from typing import Literal, Optional, TypedDict, Union
from constants import CreditCard, Transaction
from utils import parse_date, to_dict_array


def parse_category_from_description(
    *, category: str, base_description: str
) -> Optional[str]:
    description = base_description.upper()

    if "WHOLEFDS" in description:
        return {"category": "Groceries", "sub_category": "Whole Foods"}
    elif (
        "NETFLIX.COM" in description
        or "HULU" in description
        or "SPOTIFY" in description
    ):
        return {"category": "Entertainment", "sub_category": "Streaming"}
    elif "KAGI.COM" in description:
        return {"category": "Online Tools", "sub_category": "Search Engines"}
    elif "IMAX THEATRE INDIANAPOLIS" in description:
        return {"category": "Entertainment", "sub_category": "Movie Theatres"}
    elif "OLD NATIONAL CENTER" in description:
        return {"category": "Entertainment", "sub_category": "Shows/Concerts"}
    elif "ROASTING" in description:
        return {"category": "Dining", "sub_category": "Coffee"}
    elif "TARGET        " in description:
        return {"category": "Groceries", "sub_category": "Target"}
    elif "RACQUET" in description or "TENNIS" in description:
        return {"category": "Recreation", "sub_category": "Tennis"}
    elif "FUSEK'S TRUE VALUE" in description or "THE HOME DEPOT" in description:
        return {"category": "Home Improvement", "sub_category": "Hardware Stores"}
    elif (
        "SOUTHWES    " in description
        or "DELTA AIR" in description
        or "FRONTIER" in description
        or "AIRLINE" in description
        or "AIR FRANCE" in description
    ):
        return {"category": "Travel", "sub_category": "Flights"}
    elif "MISTER SPARKY-INDY" == description:
        return {"category": "Home Improvement", "sub_category": "Electricians"}
    elif (
        "HOTELS" in description
        or "INN" in description
        or "HYATT" in description
        or "HILTON" in description
        or "KASA LIVING  INC." in description
    ):
        return {"category": "Travel", "sub_category": "Hotels"}
    elif "HEATING" in description or "CONTROL TECH" in description:
        return {"category": "Home Improvement", "sub_category": "HVAC"}
    elif "BEN FRANKLIN" in description:
        return {"category": "Home Improvement", "sub_category": "Plumbing"}
    elif "LS SILVER IN THE CITY" in description:
        return {"category": "Shopping", "sub_category": "Gift Shops"}
    elif "CVS/PHARMACY" in description:
        return {"category": "Drug Stores"}
    elif (
        "LS GRAY GOAT BICYCLE" in description
        or "FREEWHEELIN COMMUNITY BI" == description
    ):
        return {"category": "Shopping", "sub_category": "Bike Shops"}
    elif "MUSEUM" == description:
        return {"category": "Education", "sub_category": "Museums"}
    elif "GENTSPA AT THE HILTON" == description:
        return {"category": "Personal", "sub_category": "Hair"}
    elif "NYTIMES" in description:
        return {"category": "Entertainment", "sub_category": "Newspapers"}
    elif "PRIME VIDEO" in description:
        return {"category": "Entertainment", "sub_category": "Streaming"}
    elif (
        "AMZN MKTP" in description
        or "AMAZON.COM" in description
        or "AMAZON PRIME*" in description
    ):
        return {"category": "Shopping", "sub_category": "Amazon"}
    elif "TURBOTAX" in description or "FREETAXUSA.COM" in description:
        return {"category": "Online Tools", "sub_category": "Tax Software"}
    elif "HAMILTONCOTREASURER" in description:
        return {"category": "Taxes", "sub_category": "Property"}
    elif "SWIPE SIMPLE GATEWAY INDIANAPOLIS IN" in description:
        return {"category": "Home Improvement", "sub_category": "Other Contractors"}
    elif "USTA LEAGUES" in description or "USTA MEMBERSHIP" in description:
        return {"category": "Recreation", "sub_category": "Tennis"}
    elif (
        "NINTENDO" in description
        or "STEAM PURCHASE" in description
        or "VALVE BELLEVUE WA" in description
        or "GAIJIN GAMES" in description
        or "OCULUS" in description
    ):
        return {"category": "Entertainment", "sub_category": "Video Games"}
    elif "TOP GOLF" in description or "ROWING" in description:
        return {"category": "Recreation"}
    elif (
        "TARGET.COM" in description
        or "WALMART.COM" in description
        or "ETSY" in description
    ):
        return {"category": "Shopping", "sub_category": "Online Retailers"}
    elif "MICRO CENTER" in description:
        return {"category": "Shopping", "sub_category": "Technology"}
    elif "NAME-CHEAP.COM" in description:
        return {"category": "Online Tools", "sub_category": "Domain Hosting"}
    elif "FOREIGN TRANSACTION FEE" in description:
        return {"category": "Fees", "sub_category": "Foreign Transaction Fees"}
    elif "UBER" in description and "TRIP" in description or "LYFT" in description:
        return {"category": "Travel", "sub_category": "Ride Sharing"}
    elif "WWW.MASSAVEANIMALCLINI" in description:
        return {"category": "Veterinary"}
    elif (
        "MOUNTAIN" in description
        or "SLOPES" in description
        or "PERFECT NORTH" in description
        or "CASCADEPORTAGE" in description
    ):
        return {"category": "Recreation", "sub_category": "Skiing"}
    elif "REGISTRY" in description:
        return {"category": "Gifts"}
    elif "ATT*BILL PAYMENT" in description or "DUKE-ENERGY" in description:
        return {"category": "Utilities"}
    elif "INSURANCE" in description:
        return {"category": "Insurance"}
    elif "GIFT" in description:
        return {"category": "Shopping"}
    elif "FASTPARK" in description or "FAST PARK IND" in description:
        return {"category": "Travel", "sub_category": "Parking"}
    elif "RENT A CA" in description or "SIXT" in description:
        return {"category": "Travel", "sub_category": "Rental Cars"}
    elif "PATREON" in description:
        return {"category": "Entertainment", "sub_category": "Patreon"}
    elif "USPS.COM STAMP" in description:
        return {"category": "Services"}
    elif "CARWASH" in description:
        return {"category": "Automotive", "sub_category": "Car Wash"}
    elif "CHASE TRAVEL" in description or "PRICELN" in description:
        return {"category": "Travel", "sub_category": "Travel Portal"}
    elif "PARKINDY" in description:
        return {"category": "Automotive", "sub_category": "Parking"}
    elif description.startswith("WDW "):
        return {"category": "Travel", "sub_category": "Theme Parks"}
    elif "BCYCLE" in description:
        return {"category": "Travel", "sub_category": "Bike Share"}
    elif "HOMEGOODS" in description or "IKEA" in description:
        return {"category": "Shopping", "sub_category": "Furniture"}
    elif "ATHLETICO" in description:
        return {"category": "Medical", "sub_category": "Physical Therapy"}
    elif "MINUTECLINIC" in description:
        return {"category": "Medical", "sub_category": "Quick/Urgent Care"}
    elif "PSVJ *JPMC FEE".upper() in description:
        return {"category": "Fees", "sub_category": "Transaction Fees"}

    return None


def parse_category(*, category: str, base_description: str):
    category_info = parse_category_from_description(
        category=category, base_description=base_description
    )

    if category_info:
        return category_info

    if "Hardware Supplies" in category:
        return {"category": "Home Improvement"}
    elif category in {"Groceries", "Merchandise & Supplies-Groceries"}:
        return {"category": "Groceries", "sub_category": "Grocery Stores"}
    elif category in {
        "Entertainment",
        "Entertainment-General Attractions",
        "Entertainment-Theatrical Events",
        "Travel/ Entertainment",
    }:
        return {"category": "Entertainment"}
    elif category in {
        "Entertainment-General Events",
        "Entertainment-Theatrical Events",
    }:
        return {"category": "Entertainment", "sub_category": "Shows/Concerts"}
    elif category in {"Gas", "Transportation-Fuel", "Gasoline"}:
        return {"category": "Gas"}
    elif category in {"Bills & Utilities", "Communications-Cable & Internet Comm"}:
        return {"category": "Utilities"}
    elif category in {"Home", "Home Improvement"}:
        return {"category": "Home Improvement"}
    elif category == "Travel":
        return {"category": "Travel"}
    elif category == "Travel-Airline":
        return {"category": "Travel", "sub_category": "Flights"}
    elif category == "Transportation-Parking Charges":
        return {"category": "Automotive", "sub_category": "Parking"}
    elif category in ("Food & Drink", "Restaurants", "Dining"):
        return {"category": "Dining"}
    elif "RESTAURANT" in category.upper():
        return {"category": "Dining"}
    elif category == "Merchandise & Supplies-Book Stores":
        return {"category": "Shopping", "sub_category": "Book Stores"}
    elif category in (
        "Shopping",
        "Merchandise",
        "Merchandise & Supplies-General Retail",
    ):
        return {"category": "Shopping"}
    elif (
        category
        in (
            "Merchandise & Supplies-Arts & Jewelry",
            "Merchandise & Supplies-Clothing Stores",
            "Merchandise & Supplies-Department Stores",
        )
        or category == "Department Stores"
    ):
        return {"category": "Shopping", "sub_category": "Clothes"}
    elif category == "Merchandise & Supplies-Internet Purchase":
        return {"category": "Shopping", "sub_category": "Online Retailers"}
    elif category == "Merchandise & Supplies-Sporting Goods Stores":
        return {"category": "Shopping", "sub_category": "Sporting Goods"}
    elif category == "Personal":
        return {"category": "Personal"}
    elif category in {"Gifts & Donations", "Other-Charities"}:
        return {"category": "Donations"}
    elif category == "Supermarkets":
        return {"category": "Groceries", "sub_category": "Supermarkets"}
    elif category == "Automotive":
        return {"category": "Automotive"}
    elif (
        "medical" in category.lower()
        or "healthcare" in category.lower()
        or "health care" in category.lower()
        or "Health & Wellness".lower() in category.lower()
    ):
        return {"category": "Medical"}
    elif category in (
        "Services",
        "Professional Services",
        "Business Services-Other Services",
    ):
        return {"category": "Services"}
    elif category in {"Travel-Lodging"}:
        return {"category": "Hotels"}
    elif category in {"Fees & Adjustments"}:
        return {"category": "Fees", "sub_category": "Credit Card Fees"}
    elif category in {"Merchandise & Supplies-Pharmacies"}:
        return {"category": "Drug Stores"}
    elif category in {"Transportation-Vehicle Leasing & Purchase"}:
        return {"category": "Automotive"}

    return None


class BaseRow(TypedDict):
    description: str
    amount: float
    category: str
    date: datetime.date
    type: Union[Literal["payment"], Literal["purchase"]]


def get_base_row(credit_card: CreditCard, row: dict[str, str]) -> BaseRow:
    amount = float(
        row.get("Amount", row.get("Debit", row.get("Credit"))).replace("$", "")
    )
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
        return {
            "description": row["Description"],
            "category": "Unknown",
            "amount": amount,
            "date": parse_date(date_str=row["Date"]),
            "type": (
                "payment" if row.get("Credit") == "" or amount <= 0 else "purchase"
            ),
        }
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
        original_description = base_row["description"]

        if base_row["type"] == "payment":
            continue

        category_info = parse_category(
            base_description=base_row["description"], category=original_category
        )

        if not category_info:
            category_info = {"category": "Unknown"}

        result = {
            "description": original_description,
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
