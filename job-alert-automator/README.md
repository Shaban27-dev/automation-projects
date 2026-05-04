# 🔔 Job Alert Automator

A smart Python automation tool that monitors a remote job board for new listings
matching your keywords, logs every match to Google Sheets, and sends a clean HTML
email digest — fully automated, runs on a configurable schedule with zero manual input.

---

## ✨ Features

- 🌐 Fetches live job listings from the [RemoteOK API](https://remoteok.com/api) (free, no API key required)
- 🔍 Filters by custom keywords and tags (e.g. `python`, `automation`, `django`)
- 🧹 Dual deduplication — by job ID and content fingerprint (title + company), so re-posted roles are never notified twice
- 📊 Logs every new match to Google Sheets with title, company, salary, tags, location, and URL
- 📧 Sends a formatted HTML email digest summarising new listings only
- ⏱️ Runs on a configurable schedule (default: every 6 hours)
- 🛡️ Handles errors gracefully:
  - API timeouts and network failures
  - Google Sheets authentication errors
  - SMTP authentication and email delivery failures
  - Missing or malformed listing data
- 📋 Writes a persistent `job_alert.log` file for debugging and audit trails
- ⚡ Modular architecture — fetch, sheets, and email logic cleanly separated

---

## ⏳ Time Saved

Manually checking a job board, filtering by keywords, logging matches to a spreadsheet,
and noting new listings every few hours would take roughly **10–15 minutes per session**.

| Scenario | Manual Time | Automated Time | Saved Per Day |
|---|---|---|---|
| 4 checks/day · 10–15 min each | ~40–60 min/day | ~0 min/day | **~1 hour/day** |
| Daily monitoring · 30 days | ~20–30 hrs/month | ~0 hrs/month | **~25 hours/month** |

Beyond time, this eliminates missed opportunities from forgetting to check, removes
human error in logging, and creates a permanent timestamped record of every listing seen.

**Business value:** Any client who manually monitors job boards, product listings,
freelance boards, or competitor postings can outsource that monitoring entirely to
this tool — zero ongoing cost, fully configurable, permanent paper trail in Google Sheets.

---

## 💼 Real-World Use Cases

- Monitor remote job boards and get notified of new matches automatically
- Build a searchable archive of job listings for analysis or trend tracking
- Use as a base for any listing monitor — freelance boards, tender sites, competitor pages
- Extend with Selenium scraping for sites without a public API
- Swap email for Telegram or SMS alerts for urgent matches

---

## 🧠 Skills Demonstrated

- REST API integration using `requests` with RemoteOK's public endpoint
- JSON parsing, data normalisation, and HTML entity decoding (`html.unescape`)
- Dual deduplication logic — source ID and content fingerprint (title + company hash)
- Google Sheets automation via `gspread` and OAuth2 service account authentication
- HTML email composition and delivery via `smtplib` and `EmailMessage`
- Structured logging with Python's `logging` module (console + persistent file handler)
- Scheduled task management using the `schedule` library
- Environment variable management with `python-dotenv`
- Modular project architecture — `main`, `sheets`, `notifier` cleanly separated
- Defensive error handling at every external integration point

---

## 📁 Project Structure

```
job-alert-automator/
├── .env                  # Keywords, sheet config, email credentials (not committed to Git)
├── .gitignore
├── credentials.json      # Google service account credentials (not committed to Git)
├── main.py               # Entry point — fetch, filter, deduplicate, schedule
├── sheets.py             # Google Sheets integration (gspread)
├── notifier.py           # Gmail HTML digest (smtplib)
├── seen_jobs.json        # Auto-generated deduplication cache (not committed to Git)
├── job_alert.log         # Persistent run log (not committed to Git)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/automation-projects.git
cd automation-projects/job-alert-automator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Google Sheets access

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project → enable **Google Sheets API** and **Google Drive API**
3. Create a **Service Account** → Keys → Add Key → JSON → rename to `credentials.json`
4. Place `credentials.json` in the project directory
5. Create a Google Sheet and copy its ID from the URL
6. Share the sheet with your service account email (Editor access)

### 4. Set up a Gmail App Password

Google requires an App Password for SMTP — not your main password:

1. Enable 2-Step Verification on your Google account
2. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Create an app password → copy the 16-character code

### 5. Set up environment variables

Create a `.env` file in the project directory:

```
KEYWORDS=python,automation,django
TAGS=python,backend
MAX_RESULTS=20
SHEET_ID=your_google_sheet_id_here
SHEET_NAME=Job Listings
EMAIL_SENDER=your_gmail@gmail.com
EMAIL_PASSWORD=your_16_char_app_password
EMAIL_RECIPIENT=your_gmail@gmail.com
RUN_INTERVAL_HOURS=6
```

### 6. Run the script

```bash
python main.py
```

---

## 🖥️ Example Output

```
2026-05-04 10:26:43 [INFO] Running job scan...
2026-05-04 10:26:44 [INFO] Fetched 97 total listings from RemoteOK
2026-05-04 10:26:44 [INFO] Matched: 25 | New (unseen): 20
2026-05-04 10:26:45 [INFO] Logged 20 rows to Google Sheets ✓
2026-05-04 10:26:46 [INFO] Email digest sent to you@gmail.com ✓

Scheduler running. Next scan in 6 hour(s). Press Ctrl+C to stop.
```

---

## 🤖 Automation Logic

| Step | Action |
|---|---|
| Fetch | Calls RemoteOK API and retrieves all current listings |
| Filter | Matches listings against configured keywords and tags |
| Deduplicate | Checks job ID and title+company fingerprint against `seen_jobs.json` |
| Log | Appends new matches to Google Sheets with all 7 columns |
| Notify | Sends HTML email digest with role, company, salary, tags, and direct links |
| Schedule | Repeats the full cycle every N hours indefinitely |

---

## ⚙️ Configuration Reference

| Variable | Default | Description |
|---|---|---|
| `KEYWORDS` | `python` | Comma-separated keywords matched in title and description |
| `TAGS` | `python` | Comma-separated RemoteOK tags to filter by |
| `MAX_RESULTS` | `20` | Max new listings to process per run |
| `SHEET_ID` | *(required)* | Google Sheet ID from the URL |
| `SHEET_NAME` | `Job Listings` | Name of the worksheet tab |
| `EMAIL_SENDER` | *(required)* | Your Gmail address |
| `EMAIL_PASSWORD` | *(required)* | Gmail App Password (16 chars) |
| `EMAIL_RECIPIENT` | *(required)* | Where to send the digest |
| `RUN_INTERVAL_HOURS` | `6` | How often to scan (in hours) |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `requests` | Fetch job listings from RemoteOK API |
| `gspread` | Read and write data to Google Sheets |
| `google-auth` | Authenticate with Google via service account credentials |
| `python-dotenv` | Securely load config from `.env` |
| `schedule` | Run the scan job on a recurring interval |
| `smtplib` | Send HTML email digests via Gmail SMTP |

---

## 🔒 Security Notes

- **Never commit `.env` or `credentials.json` to GitHub.** Add both to your `.gitignore`:

```
.env
credentials.json
seen_jobs.json
job_alert.log
```

- The `credentials.json` file contains your private service account key — treat it like a password.
- Always use a **Gmail App Password** for SMTP, never your real Google account password.
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

A production-style Python automation tool that monitors a remote job board, deduplicates
listings across runs, logs every match to Google Sheets, and delivers an HTML email digest
on a configurable schedule — demonstrating API integration, Google Sheets automation,
structured logging, dual deduplication logic, and modular architecture, while saving up
to 25 hours of manual monitoring per month.
