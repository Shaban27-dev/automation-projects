# 📊 SheetSync Crypto Reporter

A smart Python automation tool that fetches live cryptocurrency prices on a scheduled
interval and logs them automatically to Google Sheets — combining API integration,
Google Sheets automation, and scheduled task management for hands-free crypto tracking.

---

## ✨ Features

- 💰 Fetches live crypto prices using the [CoinGecko API](https://www.coingecko.com/en/api) (free, no API key required)
- 📊 Logs prices automatically to Google Sheets with formatted headers
- ⏱️ Runs on a configurable schedule (default: every 60 minutes)
- 🪙 Supports multiple coins and currencies — fully configurable via `.env`
- 🧠 Auto-creates the worksheet if it doesn't exist yet
- 🛡️ Handles errors gracefully:
  - API timeouts and network failures
  - Invalid or missing coin IDs
  - Google Sheets authentication errors
  - Missing or null price data
- ⚡ Runs once immediately on startup, then continues on schedule
- 🖥️ Clean terminal output with a formatted price summary on every log cycle

---

## ⏳ Time Saved

Manually checking and logging crypto prices for 3 coins once an hour would take
roughly **2–3 minutes per session** — opening the browser, visiting CoinGecko,
reading prices, switching to Sheets, and entering the data by hand.

| Scenario | Manual Time | Automated Time | Saved Per Day |
|---|---|---|---|
| 3 coins · every hour · 24 hrs | ~48–72 min/day | ~0 min/day | **~1 hour/day** |
| 3 coins · every hour · 30 days | ~24–36 hrs/month | ~0 hrs/month | **~30 hours/month** |

Beyond time, this also eliminates human error in data entry and ensures consistent,
timestamped records even while you're asleep or away.

---

## 💼 Real-World Use Cases

- Track crypto portfolio performance over time without manual effort
- Build a personal price history dataset for analysis or backtesting
- Use as a base for a price alert or trading signal system
- Extend to log stock prices, forex rates, or any scheduled API data
- Integrate with Google Data Studio for live dashboard visualisation

---

## 🧠 Skills Demonstrated

- REST API integration using `requests` with CoinGecko's free endpoint
- Google Sheets automation using `gspread` and service account credentials
- OAuth2 authentication via `google-auth` and a JSON credentials file
- Scheduled task management using the `schedule` library
- Environment variable management with `python-dotenv`
- Dynamic header generation and Google Sheets cell formatting
- Robust error handling across API, authentication, and data layers

---

## 📁 Project Structure

```
SheetSync-Crypto-Reporter/
├── .env                  # Stores Sheet ID, coin list, currency, interval (not committed to Git)
├── .gitignore
├── credentials.json      # Google service account credentials (not committed to Git)
├── main.py               # Full automation script — fetch, log, schedule
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/automation-projects.git
cd automation-projects/SheetSync-Crypto-Reporter
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Google Sheets access

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project → enable **Google Sheets API** and **Google Drive API**
3. Create a **Service Account** → download the `credentials.json` file
4. Place `credentials.json` in the project directory
5. Share your Google Sheet with the service account email (Editor access)

### 4. Set up environment variables

Create a `.env` file in the project directory:

```
SHEET_ID=your_google_sheet_id
SHEET_NAME=Crypto Price Log
COINS=bitcoin,ethereum,solana
CURRENCY=usd
LOG_INTERVAL_MINUTES=60
```

### 5. Run the script

```bash
python main.py
```

---

## 🖥️ Example Output

```
==================================================
   Crypto Price Logger
==================================================
  Coins    : bitcoin, ethereum, solana
  Currency : USD
  Interval : every 60 minute(s)
  Sheet ID : your_sheet_id_here
==================================================

[2026-04-25 23:13:00] Fetching prices...
Logged successfully:
       Bitcoin: USD 93,412.00
      Ethereum: USD 1,772.50
        Solana: USD 148.30

Scheduler running. Next log in 60 minute(s). Press Ctrl+C to stop.
```

---

## 🤖 Automation Logic

| Step | Action |
|---|---|
| Startup | Connects to Google Sheets, creates worksheet if missing, adds formatted headers |
| Fetch | Calls CoinGecko API for all configured coins in one request |
| Log | Appends a timestamped row with all coin prices to the sheet |
| Schedule | Repeats the fetch → log cycle every N minutes indefinitely |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `requests` | Fetch live crypto prices from CoinGecko API |
| `gspread` | Read and write data to Google Sheets |
| `google-auth` | Authenticate with Google via service account credentials |
| `python-dotenv` | Securely load config from `.env` |
| `schedule` | Run the logging job on a recurring interval |

---

## 🔒 Security Notes

- **Never commit `.env` or `credentials.json` to GitHub.** Add both to your `.gitignore`:

```
.env
credentials.json
```

- The `credentials.json` file contains your private service account key — treat it like a password.
- Only share your Google Sheet with the specific service account email, not publicly.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Shaban Alam**
📧 shabandev27@gmail.com

Python Developer focused on automation, APIs, and data tools.
Available for freelance work — building scripts, automation systems, and custom tools.

---

📌 **Summary**

A production-style Python automation tool that fetches live cryptocurrency prices from
CoinGecko and logs them to Google Sheets on a configurable schedule — demonstrating
API integration, Google Sheets automation, OAuth2 authentication, and scheduled task
management, while saving up to 30 hours of manual data entry per month.
