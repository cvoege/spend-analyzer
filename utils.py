import datetime
import inflection


def snakeify_english(english_str: str) -> str:
    return inflection.underscore("".join(english_str.split(" ")))


def to_dict_array(headers: list[str], values: list[list[str]]):
    results = []
    for row in values:
        result = {}
        for index, header in enumerate(headers):
            result[header] = row[index]
        results.append(result)

    return results


def parse_date(date_str: str) -> datetime.date:
    month, day, year = [int(date_part) for date_part in date_str.split("/")]
    return datetime.date(month=month, day=day, year=year)
