import datetime
from typing import Literal, NotRequired, TypedDict, Union


class SubCategory(TypedDict):
    name: str


class Category(TypedDict):
    name: str
    sub_categories: NotRequired[list[SubCategory]]


CATEGORIES: list[Category] = [
    {"name": "Dining"},
    {
        "name": "Groceries",
        "sub_categories": [{"name": "Whole Foods"}, {"name": "Target"}],
    },
    {"name": "PayPal"},
    {"name": "Gas"},
    {"name": "Amazon"},
    {"name": "Entertainment", "sub_categories": [{"name": "Streaming"}]},
    {"name": "Fitness"},
    {"name": "Home Improvement"},
    {"name": "Shopping", "sub_categories": [{"name": "Online Retailers"}]},
    {"name": "Travel"},
    {"name": "Drug Stores"},
]


class CreditCard(TypedDict):
    name: str
    brand: Union[
        Literal["American Express"],
        Literal["Citi"],
        Literal["Chase"],
        Literal["PNC"],
        Literal["Discover"],
    ]
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
    sub_category: NotRequired[str]
    date: datetime.date
    amount: float
    original_data: dict[str, str]
