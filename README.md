# automation-projects

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Open to Freelance](https://img.shields.io/badge/Freelance-Open%20to%20Work-orange)

A portfolio of production-style Python automation projects — built around real-world
use cases including live API data fetching, scheduled task automation, Google Sheets
integration, and intelligent email alert systems.

Each project is independently runnable, fully documented, and demonstrates practical
skills directly applicable to freelance and professional automation work.

📧 shabandev27@gmail.com · Open to freelance Python work

---

## 📁 Projects

### 📊 SheetSync Crypto Reporter
Fetches live cryptocurrency prices from the CoinGecko API on a configurable schedule
and automatically logs timestamped entries to Google Sheets. Uses OAuth2 service account
authentication, auto-creates worksheets, and formats headers on first run.

**Highlights:** Google Sheets API · CoinGecko API · OAuth2 · schedule · Saves ~30 hrs/month
→ [`SheetSync-Crypto-Reporter/`](./SheetSync-Crypto-Reporter)

---

### 🤖 Multi-API Alert Bot
Monitors live weather conditions and stock market movements across three APIs
(OpenWeatherMap, Alpha Vantage, NewsAPI). Sends formatted email alerts with contextual
advice and related news headlines when thresholds are exceeded. Modular architecture
with shared config, reusable email utility, and persistent error logging.

**Highlights:** 3-API integration · threshold-based alerts · modular design · error.log
→ [`multi_api_alert_bot/`](./multi_api_alert_bot)

---

### 😂 Smart Joke Email Automator
Fetches a random joke from a public API, stores jokes locally in a JSON history file,
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
| **HTTP & APIs** | requests · CoinGecko · OpenWeatherMap · Alpha Vantage · NewsAPI |
| **Google Integration** | gspread · google-auth · Google Sheets API · Google Drive API |
| **Email** | smtplib · EmailMessage |
| **Scheduling** | schedule |
| **Config & Security** | python-dotenv · .env files · service account credentials |
| **Data Storage** | JSON · Google Sheets |

---

## 🧠 What These Projects Demonstrate

- Multi-API integration using `requests` with real-world, production endpoints
- Google Sheets automation via `gspread` and OAuth2 service account authentication
- Scheduled task management with the `schedule` library for hands-free automation
- Email automation via `smtplib` with SMTP authentication and formatted delivery
- Threshold-based alert logic and conditional workflow triggers
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
# Example — SheetSync Crypto Reporter
cd SheetSync-Crypto-Reporter
pip install -r requirements.txt
python main.py
```

```bash
# Example — Multi-API Alert Bot
cd multi_api_alert_bot
pip install -r requirements.txt
python main.py
```

All projects require **Python 3** and a small set of pip-installable dependencies.

---

## 🔮 Future Improvements

- [ ] Add a Telegram bot integration for alert delivery alongside email
- [ ] Build a unified dashboard to run all tools from a single CLI menu
- [ ] Add pytest unit tests for API fetch and data processing logic
- [ ] Containerise projects with Docker for portable, environment-free deployment
- [ ] Add GitHub Actions workflow to run the crypto logger on a cloud schedule

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
