# automation-projects

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Projects](https://img.shields.io/badge/Projects-8-blueviolet)
![Open to Freelance](https://img.shields.io/badge/Freelance-Open%20to%20Work-orange)

A portfolio of production-style Python automation projects — covering webhook relay
servers, live API monitoring, Google Sheets integration, scheduled email systems,
job board automation, and CLI productivity tools.

Every project in this repo solves a real, repeatable problem that a business or
individual would otherwise handle manually. Each is independently runnable, fully
documented, and built to a standard directly applicable to freelance and professional
automation work.

📧 shabandev27@gmail.com · Open to freelance Python work

---

## ✨ What This Repo Demonstrates

This is not a collection of exercises — these are working tools:

- **Receiving** and routing live webhook events with token-authenticated Flask endpoints
- **Monitoring** live data sources — crypto prices, weather, stocks, and job boards
- **Alerting** via formatted HTML email when thresholds are crossed or new events arrive
- **Logging** structured data to Google Sheets automatically on a schedule
- **Deduplicating** records across runs so nothing is notified twice
- **Automating** file organisation, phonetic conversion, and desktop timers via CLI
- **Running hands-free** — scheduled, persistent, zero manual input after setup

---

## ⏳ Time Saved Across All Projects

| Project | Task Automated | Estimated Saving |
|---|---|---|
| 📊 SheetSync Crypto Reporter | Manual price checks + Sheets entry | **~30 hrs/month** |
| 🔔 Job Alert Automator | Manual job board checks + logging | **~25 hrs/month** |
| 🔗 Flask Webhook Relay | Manual payload monitoring + email formatting | **~15 hrs/month** |
| 🤖 Multi-API Alert Bot | Manual weather + stock monitoring | **~10 hrs/month** |
| 🌦️ Weather API Fetcher | Manual weather lookups + note-taking | **~3 hrs/month** |
| 😂 Smart Joke Email Automator | Manual content curation + sending | **~2 hrs/month** |
| 🗂️ CLI Tools (×3) | Manual file sorting, lookups, time tracking | **~5 hrs/month** |

**Total estimated saving: ~90 hours/month** across all tools running together.

**Business value:** Any client who manually monitors APIs, sorts files, checks job
boards, or sends recurring emails can outsource that entire workflow to Python — zero
ongoing cost, fully configurable, runs while they sleep, permanent paper trail.

---

## 📁 Projects

### 🔗 Flask Webhook Relay
A production-ready Flask server that receives incoming webhook payloads, authenticates
requests via a secret token, prints structured logs to the terminal, and fires a
formatted HTML email alert for every valid event. Built to integrate directly with
n8n, Zapier, or any webhook-capable tool. Includes a `/health` liveness endpoint
and a browser-based `/test` UI — no Postman required.

**Highlights:** Flask routing · decorator-based token auth · HTML email · structured logging · n8n compatible
→ [`flask-webhook-relay/`](./flask-webhook-relay)

---

### 🔔 Job Alert Automator
Monitors RemoteOK for new job listings matching your keywords, deduplicates by job
ID and content fingerprint across runs, logs every match to Google Sheets, and sends
a clean HTML email digest — fully automated on a configurable schedule.

**Highlights:** Dual deduplication · HTML digest · Google Sheets logging · audit log · saves ~25 hrs/month
→ [`job-alert-automator/`](./job-alert-automator)

---

### 📊 SheetSync Crypto Reporter
Fetches live cryptocurrency prices from the CoinGecko API on a configurable schedule
and automatically logs timestamped rows to Google Sheets. Auto-creates worksheets
and formats headers on first run — zero manual setup after initial config.

**Highlights:** CoinGecko API · Google Sheets API · OAuth2 · schedule · saves ~30 hrs/month
→ [`SheetSync-Crypto-Reporter/`](./SheetSync-Crypto-Reporter)

---

### 🤖 Multi-API Alert Bot
Monitors live weather conditions and stock market movements across three APIs
(OpenWeatherMap, Alpha Vantage, NewsAPI). Sends formatted email alerts with contextual
advice and related news headlines when thresholds are exceeded. Fully modular with
shared config, reusable email utility, and persistent error logging.

**Highlights:** 3-API integration · threshold-based alerts · modular architecture · error.log
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

### 🗂️ CLI Tools

A set of focused command-line utilities demonstrating clean Python scripting, standard
library mastery, and real-world productivity automation — no unnecessary dependencies.

#### 🗃️ File Organizer
Scans a folder and automatically sorts files into subfolders by type (images, documents,
videos, etc.). Handles edge cases — duplicates, unknown extensions, nested folders.

**Highlights:** `os` · `shutil` · pure stdlib · zero dependencies
→ [`cli-tools/File-Organizer/`](./cli-tools/File-Organizer)

#### 🔤 NATO Alphabet Converter
Converts any word or sentence into NATO phonetic codes using a Pandas CSV lookup.
Handles mixed case, ignores non-alphabetic characters, and outputs clean formatted results.

**Highlights:** Pandas · CSV lookup · input validation · clean CLI output
→ [`cli-tools/NATO-Alphabet-Converter/`](./cli-tools/NATO-Alphabet-Converter)

#### ⏱️ Pomodoro Timer
Desktop productivity timer built with Tkinter. Runs automatic 25/5/15-minute work and
break cycles, tracks completed sessions with checkmarks, and resets cleanly.

**Highlights:** Tkinter GUI · event loop · session tracking · desktop automation
→ [`cli-tools/Pomodoro-Timer/`](./cli-tools/Pomodoro-Timer)

---

## 🛠️ Stack

| Layer | Tools |
|---|---|
| **Language** | Python 3 |
| **Web Framework** | Flask |
| **HTTP & APIs** | requests · CoinGecko · OpenWeatherMap · Alpha Vantage · NewsAPI · RemoteOK |
| **Google Integration** | gspread · google-auth · Google Sheets API · Google Drive API |
| **Email** | smtplib · MIMEMultipart · HTML email composition |
| **Scheduling** | schedule |
| **Logging** | logging module · persistent file handlers |
| **Config & Security** | python-dotenv · .env files · token auth · service account credentials |
| **Data Storage** | JSON · Google Sheets |
| **Desktop GUI** | Tkinter |
| **Data Processing** | Pandas · os · shutil |

---

## 🧠 Skills Demonstrated

- Flask web server — routing, request handling, JSON responses, middleware decorators
- Python decorators — `@require_token` auth wrapping protected routes
- Multi-API integration using `requests` with real-world, production endpoints
- Google Sheets automation via `gspread` and OAuth2 service account authentication
- HTML email composition — inline CSS, dynamic tables, `MIMEMultipart` structure
- Email delivery via `smtplib` — plain text and HTML digest formats
- Scheduled task management with `schedule` for hands-free, recurring automation
- Dual deduplication — by source ID and content fingerprint across persistent runs
- Structured logging with Python's `logging` module (console + persistent file)
- Threshold-based alert logic and conditional workflow triggers
- Secure credential management with `.env` files, `python-dotenv`, and token auth
- Modular project architecture — config, utils, and workflows cleanly separated
- Persistent local data storage using JSON read/write cycles
- Robust error handling across HTTP, SMTP, authentication, and data layers
- Desktop GUI development with Tkinter event loops and session management
- File system automation using `os` and `shutil`
- Data lookup and transformation with Pandas and CSV

---

## 🚀 Run Any Project

Each project folder contains its own `README.md` with full setup and run instructions.

```bash
# Flask Webhook Relay
cd flask-webhook-relay
pip install -r requirements.txt
python app.py
```

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
# CLI Tools — File Organizer
cd cli-tools/File-Organizer
python main.py
```

All projects require **Python 3**. API and Google integrations require a small set
of pip-installable dependencies listed in each project's `requirements.txt`.

---

## 🔒 Security Notes

All credentials and secrets are managed securely across every project in this repo:

- **Never commit `.env` or `credentials.json` to GitHub** — both are listed in each project's `.gitignore`
- `.env` files store API keys, webhook secrets, email credentials, and sheet IDs — loaded at runtime via `python-dotenv`
- `credentials.json` contains Google service account private keys — treat like a password
- The Flask webhook endpoint is protected by a secret token — requests without it are rejected with `401`
- Gmail SMTP always uses **App Passwords**, never your real Google account password
- Google Sheets are shared only with the specific service account email, not publicly

```
# Common .gitignore entries across all projects
.env
credentials.json
seen_jobs.json
job_alert.log
webhook.log
error.log
```

---

## 🔮 Future Improvements

- [ ] Add Telegram bot integration for alert delivery alongside email
- [ ] Deploy Flask Webhook Relay to a cloud server (Railway, Render, or DigitalOcean) for 24/7 uptime
- [ ] Build a unified CLI dashboard to run all tools from a single entry point
- [ ] Add `pytest` unit tests for API fetch, deduplication, and data processing logic
- [ ] Containerise projects with Docker for portable, environment-free deployment
- [ ] Add GitHub Actions workflow to run the crypto logger on a cloud schedule
- [ ] Extend the job monitor with Selenium scraping for non-API job sites

---

## 📄 License

This repository is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Contact

**Shaban Alam**
📧 shabandev27@gmail.com
🐙 [github.com/Shaban27-dev](https://github.com/Shaban27-dev)

I build Python automation scripts, Flask APIs, Google Sheets integrations, webhook
systems, and email tools. If you have a repetitive task that Python can handle — I
can build it.

---

📌 **Summary**

A portfolio of eight production-style Python automation tools — spanning a Flask
webhook relay server, live API monitoring, Google Sheets automation, scheduled email
delivery, job board tracking, and CLI productivity utilities. Every project demonstrates
modular architecture, robust error handling, secure credential management, and real-world
automation design patterns. Combined, these tools save an estimated 90 hours of manual
work per month and are directly deployable for freelance client use.
