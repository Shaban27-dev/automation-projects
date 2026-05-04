# automation-projects

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Projects](https://img.shields.io/badge/Projects-5-blueviolet)
![Open to Freelance](https://img.shields.io/badge/Freelance-Open%20to%20Work-orange)

A portfolio of production-style Python automation projects — built around real-world
use cases including live API data fetching, Google Sheets integration, scheduled task
automation, intelligent email alert systems, and job board monitoring.

Each project is independently runnable, fully documented, and demonstrates practical
skills directly applicable to freelance and professional automation work.

📧 shabandev27@gmail.com · Open to freelance Python work

---

## ✨ What This Repo Demonstrates

This is not a collection of exercises — every project in this repo solves a real,
repeatable problem that a business or individual would otherwise handle manually:

- **Monitoring** live data sources (crypto prices, weather, stocks, job boards)
- **Alerting** via email when thresholds are crossed or new matches appear
- **Logging** structured data to Google Sheets automatically on a schedule
- **Deduplicating** records across runs so nothing gets notified twice
- **Running hands-free** — scheduled, persistent, and zero manual input after setup

---

## ⏳ Time Saved Across All Projects

| Project | Task Automated | Estimated Saving |
|---|---|---|
| 📊 SheetSync Crypto Reporter | Manual price checks + Sheets entry | **~30 hrs/month** |
| 🔔 Job Alert Automator | Manual job board checks + logging | **~25 hrs/month** |
| 🤖 Multi-API Alert Bot | Manual weather + stock monitoring | **~10 hrs/month** |
| 😂 Smart Joke Email Automator | Manual content curation + sending | **~2 hrs/month** |
| 🌦️ Weather API Fetcher | Manual weather lookups + note-taking | **~3 hrs/month** |

**Total estimated saving: ~70 hours/month** across all five tools running together.

**Business value:** Any client who manually monitors APIs, logs data, or sends
recurring emails can outsource that work entirely to Python — zero ongoing cost,
fully configurable, permanent paper trail, runs while they sleep.

---

## 📁 Project Highlights

### 🔔 Job Alert Automator
Monitors RemoteOK for new listings matching your keywords, deduplicates by job ID
and content fingerprint, logs every match to Google Sheets, and sends an HTML email
digest — all on a configurable schedule.

**Highlights:** Dual deduplication · HTML email digest · Google Sheets logging · structured logging · saves ~25 hrs/month
→ [`job-alert-automator/`](./job-alert-automator)

---

### 📊 SheetSync Crypto Reporter
Fetches live cryptocurrency prices from the CoinGecko API on a configurable schedule
and automatically logs timestamped entries to Google Sheets. Auto-creates worksheets
and formats headers on first run.

**Highlights:** CoinGecko API · Google Sheets API · OAuth2 · schedule · saves ~30 hrs/month
→ [`SheetSync-Crypto-Reporter/`](./SheetSync-Crypto-Reporter)

---

### 🤖 Multi-API Alert Bot
Monitors live weather conditions and stock market movements across three APIs
(OpenWeatherMap, Alpha Vantage, NewsAPI). Sends formatted email alerts with contextual
advice and related news headlines when thresholds are exceeded.

**Highlights:** 3-API integration · threshold-based alerts · modular design · error.log
→ [`multi_api_alert_bot/`](./multi_api_alert_bot)

---

### 😂 Smart Joke Email Automator
Fetches a random joke from a public API, stores jokes in a local JSON history file,
and automatically emails a random joke every Sunday. Includes retry logic for API
failures and graceful handling of corrupted local data.

**Highlights:** Scheduled email delivery · JSON persistence · retry logic · smtplib
→ [`smart-joke-email-automator/`](./smart-joke-email-automator)

---

### 🌦️ Weather API Fetcher
Connects to the OpenWeatherMap API to retrieve live weather data for any city.
Provides smart contextual advice based on temperature and conditions, and maintains
a rolling local JSON history log capped at 50 entries.

**Highlights:** OpenWeatherMap API · smart advice logic · JSON history tracking
→ [`weather-api-fetcher/`](./weather-api-fetcher)

---

## 🛠️ Stack

| Layer | Tools |
|---|---|
| **Language** | Python 3 |
| **HTTP & APIs** | requests · CoinGecko · OpenWeatherMap · Alpha Vantage · NewsAPI · RemoteOK |
| **Google Integration** | gspread · google-auth · Google Sheets API · Google Drive API |
| **Email** | smtplib · EmailMessage |
| **Scheduling** | schedule |
| **Logging** | logging module · persistent file handlers |
| **Config & Security** | python-dotenv · .env files · service account credentials |
| **Data Storage** | JSON · Google Sheets |

---

## 🧠 Skills Demonstrated

- Multi-API integration using `requests` with real-world, production endpoints
- Google Sheets automation via `gspread` and OAuth2 service account authentication
- Scheduled task management with `schedule` for hands-free, recurring automation
- Email automation via `smtplib` — plain text and HTML digest formats
- Threshold-based alert logic and conditional workflow triggers
- Dual deduplication — by source ID and content fingerprint across runs
- Structured logging with Python's `logging` module (console + persistent file)
- Secure credential management using `.env` files and `python-dotenv`
- Modular project architecture — config, utils, and workflows cleanly separated
- Persistent local data storage using JSON read/write cycles
- Robust error handling across HTTP, network, authentication, and data layers
- Clean CLI design with input validation and formatted terminal output

---

## 🚀 Run Any Project

Each project folder contains its own `README.md` with full setup and run instructions,
including environment variable configuration and dependency installation.

```bash
# Job Alert Automator
cd job-alert-automator
pip install -r requirements.txt
python main.py
```

```bash
# SheetSync Crypto Reporter
cd SheetSync-Crypto-Reporter
pip install -r requirements.txt
python main.py
```

```bash
# Multi-API Alert Bot
cd multi_api_alert_bot
pip install -r requirements.txt
python main.py
```

All projects require **Python 3** and a small set of pip-installable dependencies.

---

## 🔒 Security Notes

All credentials and secrets are managed securely across every project in this repo:

- **Never commit `.env` or `credentials.json` to GitHub** — both are listed in each project's `.gitignore`
- `.env` files store API keys, email credentials, and sheet IDs — loaded at runtime via `python-dotenv`
- `credentials.json` contains Google service account private keys — treat like a password
- Gmail SMTP always uses **App Passwords**, never your real Google account password
- Google Sheets are shared only with the specific service account email, not publicly

```
# Typical .gitignore entries across all projects
.env
credentials.json
seen_jobs.json
job_alert.log
error.log
*.json   # for auto-generated data files
```

---

## 🔮 Future Improvements

- [ ] Add Telegram bot integration for alert delivery alongside email
- [ ] Build a unified CLI dashboard to run all tools from a single entry point
- [ ] Add `pytest` unit tests for API fetch and data processing logic
- [ ] Containerise projects with Docker for portable, environment-free deployment
- [ ] Add GitHub Actions workflow to run the crypto logger on a cloud schedule
- [ ] Add Selenium scraping module to extend job monitor to non-API sites

---

## 📄 License

This repository is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Contact

**Shaban Alam**
📧 shabandev27@gmail.com
🐙 [github.com/Shaban27-dev](https://github.com/Shaban27-dev)

I build Python automation scripts, API integrations, Google Sheets tools, and email
systems. If you have a repetitive task that Python can handle — I can build it.

---

📌 **Summary**

A portfolio of five production-style Python automation tools covering API integration,
Google Sheets automation, scheduled email delivery, job board monitoring, and intelligent
alert systems — demonstrating modular architecture, robust error handling, secure credential
management, and real-world automation design patterns. Combined, these tools save an
estimated 70 hours of manual work per month.
