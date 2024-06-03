import datetime
from typing import Literal, NotRequired, TypedDict, Union


class SubCategory(TypedDict):
    name: str


class Category(TypedDict):
    name: str
    sub_categories: NotRequired[list[SubCategory]]


CATEGORIES: list[Category] = [
    {"name": "Dining", "sub_categories": {"name": "Coffee"}},
    {
        "name": "Groceries",
        "sub_categories": [
            {"name": "Grocery Stores"},
            {"name": "Book Stores"},
            {"name": "Whole Foods"},
            {"name": "Target"},
            {"name": "Supermakerts"},
            {"name": "Walmart"},
        ],
    },
    {"name": "Gas"},
    {
        "name": "Entertainment",
        "sub_categories": [
            {"name": "Streaming"},
            {"name": "Movie Theatres"},
            {"name": "Bars"},
            {"name": "Newspapers"},
            {"name": "Video Games"},
            {"name": "Shows/Concerts"},
        ],
    },
    {
        "name": "Recreation",
        "sub_categories": [
            {"name": "Skiing"},
            {"name": "State/National Parks"},
            {"name": "Tennis"},
            {"name": "Gym & Community Center"},
        ],
    },
    {
        "name": "Home Improvement",
        "sub_categories": [
            {"name": "Hardware Stores"},
            {"name": "Electricians"},
            {"name": "Plumbers"},
            {"name": "HVAC"},
            {"name": "Other Contractors"},
        ],
    },
    {
        "name": "Shopping",
        "sub_categories": [
            {"name": "Online Retailers"},
            {"name": "Amazon"},
            {"name": "Gift Shops"},
            {"name": "Bike Shops"},
            {"name": "Technology"},
            {"name": "Department Stores"},
            {"name": "Sporting Goods"},
            {"name": "Furniture"},
            {"name": "Clothes"},
        ],
    },
    {
        "name": "Travel",
        "sub_categories": [
            {"name": "Flights"},
            {"name": "Hotels"},
            {"name": "Ride Sharing"},
            {"name": "Bike Share"},
            {"name": "Rental Cars"},
            {"name": "Parking"},
            {"name": "Travel Portal"},
            {"name": "Theme Parks"},
        ],
    },
    {
        "name": "Online Tools",
        "sub_categories": [
            {"name": "Search Engines"},
            {"name": "Tax Software"},
            {"name": "Domain Hosting"},
        ],
    },
    {"name": "Drug Stores"},
    {"name": "Taxes", "sub_categories": [{"name": "Property"}]},
    {
        "name": "Medical",
        "sub_categories": [
            {"name": "Primary Care"},
            {"name": "Quick/Urgent Care"},
            {"name": "Emergency Care"},
            {"name": "Insurance Premiums"},
            {"name": "Physical Therapy"},
        ],
    },
    {"name": "Veterinary"},
    {"name": "Insurance"},
    {
        "name": "Automotive",
        "sub_categories": [
            {"name": "Maintenance"},
            {"name": "Parking"},
            {"name": "Car Wash"},
        ],
    },
    {"name": "Utilities"},
    {"name": "Services"},
    {"name": "Donations"},
    {"name": "Gifts"},
    {"name": "Personal", "sub_categories": [{"name": "Hair"}]},
    {"name": "Education", "sub_categories": [{"name": "Museums"}]},
    {
        "name": "Fees",
        "sub_categories": [
            {
                "name": "Foreign Transaction Fees",
            },
            {"name": "Credit Card Fees"},
            {"name": "Transaction Fees"},
            {"name": "Bank Fees"},
        ],
    },
]

CreditCardBrand = Union[
    Literal["American Express"],
    Literal["Citi"],
    Literal["Chase"],
    Literal["PNC"],
    Literal["Discover"],
]


class CreditCard(TypedDict):
    name: str
    brand: CreditCardBrand
    foreign_transaction_fees: bool
    base_cash_back_rate: float
    category_cash_back_rates: NotRequired[dict[str, float]]
    rotating_cash_back_rate: NotRequired[float]
    known_categories: NotRequired[list[str]]
    top_category_cash_back_rate: NotRequired[float]
    top_category_rate_spend_max: NotRequired[float]


CREDIT_CARDS: list[CreditCard] = [
    {
        "name": "American Express Blue Cash Everyday",
        "brand": "American Express",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.01,
        "category_cash_back_rates": {
            "Groceries": 0.03,
            "Gas": 0.03,
            "Online Retailers": 0.03,
        },
    },
    {
        "name": "American Express Blue Cash Preferred",
        "brand": "American Express",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.01,
        "category_cash_back_rates": {
            "Groceries": 0.06,
            "Gas": 0.03,
            "Online Retailers": 0.03,
        },
    },
    {
        "name": "Chase Freedom Unlimited",
        "brand": "Chase",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.015,
    },
    {
        "name": "Amazon Visa",
        "brand": "Chase",
        "foreign_transaction_fees": False,
        "base_cash_back_rate": 0.01,
        "category_cash_back_rates": {
            "Groceries": 0.03,
            "Gas": 0.03,
            "Online Retailers": 0.03,
        },
    },
    {
        "name": "Chase Freedom Flex",
        "brand": "Chase",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.01,
        "category_cash_back_rates": {
            "Travel": 0.05,
            "Dining": 0.03,
            "Drug Stores": 0.03,
        },
    },
    {
        "name": "Chase Sapphire Preferred",
        "brand": "Chase",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.01,
        "rotating_cash_back_rate": 0.05,
        "known_categories": [
            "Dining",
            "Groceries",
            "PayPal",
            "Gas",
            "Target",
            "Amazon",
        ],
    },
    {
        "name": "Discover It",
        "brand": "Discover",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.01,
        "rotating_cash_back_rate": 0.05,
        "known_categories": [
            "Dining",
            "Groceries",
            "PayPal",
            "Gas",
            "Target",
            "Amazon",
        ],
    },
    {
        "name": "PNC Cash Rewards",
        "brand": "PNC",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.01,
        "category_cash_back_rates": {
            "Gas": 0.04,
            "Dining": 0.03,
            "Groceries": 0.02,
        },
    },
    {
        "name": "Citi Double Cash",
        "brand": "Citi",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.02,
    },
    {
        "name": "PNC Cashbuilder",
        "brand": "PNC",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.015,
    },
    {
        "name": "Citi Custom Cash",
        "brand": "Citi",
        "foreign_transaction_fees": True,
        "base_cash_back_rate": 0.01,
        "top_category_cash_back_rate": 0.05,
        "top_category_rate_spend_max": 500,
    },
]


class Transaction(TypedDict):
    description: str
    category: str
    sub_category: str
    original_category: str
    credit_card_name: str
    date: datetime.date
    amount: float
    original_data: dict[str, str]


class TransactionData(TypedDict):
    transaction_sheet_name: str
    credit_card: str
    transactions: list[Transaction]


class IndexData(TypedDict):
    transaction_sheet_name: str
    credit_card: str


class SheetMetadataProperties(TypedDict):
    title: str


class SheetMetadata(TypedDict):
    properties: SheetMetadataProperties
