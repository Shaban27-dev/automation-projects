import os
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

HEADERS = ["Date Found", "Title", "Company", "Tags", "Salary", "Location", "URL"]


def _connect(sheet_id: str, sheet_name: str):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    creds_path = os.path.join(base_dir, "credentials.json")
    creds = Credentials.from_service_account_file(creds_path, scopes=SCOPES)
    
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(sheet_id)
    try:
        ws = spreadsheet.worksheet(sheet_name)
    except gspread.WorksheetNotFound:
        ws = spreadsheet.add_worksheet(title=sheet_name, rows=2000, cols=len(HEADERS))
        print(f"  Created worksheet: '{sheet_name}'")
    return ws

def _ensure_headers(ws):
    if not ws.row_values(1):
        ws.append_row(HEADERS)


def log_jobs(jobs: list[dict], sheet_id: str, sheet_name: str) -> int:
    """Append new jobs to the sheet. Returns count of rows added."""
    if not jobs:
        return 0

    ws = _connect(sheet_id, sheet_name)
    _ensure_headers(ws)

    rows = [
        [
            job.get("date_found", ""),
            job.get("title", ""),
            job.get("company", ""),
            job.get("tags", ""),
            job.get("salary", "N/A"),
            job.get("location", "Remote"),
            job.get("url", ""),
        ]
        for job in jobs
    ]

    ws.append_rows(rows, value_input_option="USER_ENTERED")
    return len(rows)
