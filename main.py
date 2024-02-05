import os.path
import os
import json
from pprint import pprint
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import inflection

from constants import CreditCard, Transaction
from parse_transactions import parse_transactions
from utils import snakeify_english

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
# SAMPLE_RANGE_NAME = "Class Data!A2:E"


def get_creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


SERVICE = build("sheets", "v4", credentials=get_creds())

# Call the Sheets API
SHEETS_API = SERVICE.spreadsheets()


def get_local_data():
    if os.path.exists("data.json"):
        with open("data.json") as f:
            return json.loads(f.read())

    return {}


def write_local_data(local_data):
    with open("data.json", "w") as f:
        f.write(json.dumps(local_data))


def get_spreadsheet_id() -> str:
    local_data = get_local_data()
    if local_data.get("spreadsheet_id"):
        return local_data["spreadsheet_id"]

    id = input("Please provide the spreadsheet id: ")
    local_data["spreadsheet_id"] = id
    write_local_data(local_data=local_data)
    return id


def get_sheets():
    spreadsheet_metadata = SHEETS_API.get(spreadsheetId=get_spreadsheet_id()).execute()
    sheets = spreadsheet_metadata["sheets"]
    return sheets


def get_index_data():
    base_index_data = (
        SHEETS_API.values()
        .get(spreadsheetId=get_spreadsheet_id(), range="Index")
        .execute()
    ).get("values", [])

    headers = base_index_data[0]
    rows = base_index_data[1:]

    index_data = []
    for row in rows:
        result_row = {}
        for index, header in enumerate(headers):
            result_row[snakeify_english(header)] = row[index]

        index_data.append(result_row)

    return index_data


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    index_data = get_index_data()

    transaction_sheet_names = [row["transaction_sheet_name"] for row in index_data]

    transaction_results = (
        SHEETS_API.values()
        .batchGet(spreadsheetId=get_spreadsheet_id(), ranges=transaction_sheet_names)
        .execute()
    )

    full_transaction_data = []
    for index_row in index_data:
        current_value_range = None
        for value_range in transaction_results["valueRanges"]:
            if value_range["range"].startswith(
                f"{index_row['transaction_sheet_name']}!"
            ):
                current_value_range = value_range
                break

        if not current_value_range:
            print(
                "Sheet index specified there would be a sheet called "
                f"{index_row['transaction_sheet_name']}, but one was not found"
            )
            sys.exit(1)

        full_transaction_data.append(
            {
                **index_row,
                "transactions": parse_transactions(
                    credit_card=index_row["credit_card"],
                    headers=current_value_range["values"][0],
                    values=current_value_range["values"][1:],
                ),
            }
        )

    # values = result.get("values", [])

    # if not values:
    #   print("No data found.")
    #   return

    # print("Name, Major:")
    # for row in values:
    #   # Print columns A and E, which correspond to indices 0 and 4.
    #   print(f"{row[0]}, {row[4]}")


if __name__ == "__main__":
    main()
