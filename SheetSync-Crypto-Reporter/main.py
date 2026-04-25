import os
import time
import requests
import gspread
import schedule
from datetime import datetime
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

# ── Config ────────────────────────────────────────────────────────────────────

SHEET_ID = os.getenv("SHEET_ID")
SHEET_NAME = os.getenv("SHEET_NAME", "Crypto Price Log")
COINS = [c.strip() for c in os.getenv("COINS", "bitcoin,ethereum,solana").split(",")]
CURRENCY = os.getenv("CURRENCY", "usd").lower()
INTERVAL = int(os.getenv("LOG_INTERVAL_MINUTES", 60))

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

# ── Google Sheets connection ──────────────────────────────────────────────────

def connect_to_sheet():
    """Authenticate and return the target worksheet."""
    json_path = r"C:\Users\Lenovo\classroom\automation-projects\SheetSync-Crypto-Reporter\credentials.json"
    creds = Credentials.from_service_account_file(json_path, scopes=SCOPES)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(SHEET_ID)

    # Get or create the worksheet
    try:
        worksheet = spreadsheet.worksheet(SHEET_NAME)
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=SHEET_NAME, rows=1000, cols=20)
        print(f"Created new worksheet: {SHEET_NAME}")

    return worksheet


def ensure_headers(worksheet):
    """Add header row if the sheet is empty."""
    first_row = worksheet.row_values(1)
    if not first_row:
        headers = ["Timestamp"] + [coin.capitalize() + f" ({CURRENCY.upper()})" for coin in COINS]
        worksheet.append_row(headers)
        # changes
        last_col_letter = chr(64 + len(headers))
        header_range = f"A1:{last_col_letter}1"
        worksheet.format(header_range, {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER", "backgroundColor": {"red": 0.9, "green": 0.9, "blue": 0.9}})
        print(f"Added and formatted headers: {headers}")

# ── Data fetching ─────────────────────────────────────────────────────────────

def fetch_prices():
    """Fetch live prices from CoinGecko (free, no API key needed)."""
    params = {
        "ids": ",".join(COINS),
        "vs_currencies": CURRENCY,
    }

    try:
        response = requests.get(COINGECKO_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        prices = []
        for coin in COINS:
            price = data.get(coin, {}).get(CURRENCY)
            if price is None:
                print(f"Warning: Could not get price for '{coin}'. Check coin ID.")
            prices.append(price)

        return prices

    except requests.exceptions.RequestException as e:
        print(f"Error fetching prices: {e}")
        return None

# ── Logging ───────────────────────────────────────────────────────────────────

def log_prices():
    """Main job: fetch prices and append a row to Google Sheets."""
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetching prices...")

    prices = fetch_prices()
    if prices is None:
        print("Skipping this cycle due to fetch error.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp] + prices

    try:
        worksheet = connect_to_sheet()
        ensure_headers(worksheet)
        worksheet.append_row(row)

        # Pretty print to terminal
        print("Logged successfully:")
        for coin, price in zip(COINS, prices):
            if price is not None:
                print(f"  {coin.capitalize():>12}: {CURRENCY.upper()} {price:,.2f}")
    except Exception as e:
        print(f"Error writing to sheet: {e}")

# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("   Crypto Price Logger")
    print("=" * 50)
    print(f"  Coins    : {', '.join(COINS)}")
    print(f"  Currency : {CURRENCY.upper()}")
    print(f"  Interval : every {INTERVAL} minute(s)")
    print(f"  Sheet ID : {SHEET_ID}")
    print("=" * 50)

    # Run once immediately on startup
    log_prices()

    # Then schedule recurring runs
    schedule.every(INTERVAL).minutes.do(log_prices)

    print(f"\nScheduler running. Next log in {INTERVAL} minute(s). Press Ctrl+C to stop.\n")

    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()
