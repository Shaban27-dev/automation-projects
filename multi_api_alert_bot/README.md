# 🤖 Multi-API Alert Bot

A smart Python automation tool that monitors real-time weather conditions and stock market
movements, then automatically sends email alerts with contextual advice and relevant news —
combining multi-API integration, modular design, and email automation.

---

## ✨ Features

- 🌦️ Fetches live weather data using the [OpenWeatherMap API](https://openweathermap.org/api)
- 📈 Tracks daily stock price changes using the [Alpha Vantage API](https://www.alphavantage.co/)
- 📰 Fetches related news headlines using the [NewsAPI](https://newsapi.org/)
- 📧 Sends formatted email alerts automatically when thresholds are exceeded
- 🧠 Smart assistant logic — contextual weather advice based on temperature and conditions
- 🛡️ Handles errors gracefully:
  - API timeouts and network failures
  - Invalid city names or stock symbols
  - API rate limits and unexpected response formats
  - SMTP authentication and email delivery failures
- 📋 Logs all errors to a local `error.log` file for debugging
- ⚡ Clean modular CLI tool — each concern separated into its own module

---

## 💼 Real-World Use Cases

- Automate weather alerts before extreme conditions hit
- Monitor stock volatility and get notified on big moves
- Use as a base for a personal finance or trading notification bot
- Extend into a full daily briefing system (weather + stocks + news)
- Integrate with cron jobs or task schedulers for hands-free automation

---

## 🧠 Skills Demonstrated

- Multi-API integration using `requests` (weather, stocks, news)
- Email automation using `smtplib` and `EmailMessage`
- Environment variable management with `python-dotenv`
- Modular Python project structure (config, utils, workflows)
- Threshold-based alert logic and conditional email triggers
- Robust error handling across network, HTTP, and SMTP layers
- Persistent error logging with timestamps

---

## 📁 Project Structure

```
multi_api_alert_bot/
├── .env                  # Stores all API keys and email credentials (not committed to Git)
├── .gitignore
├── config.py             # Loads environment variables and defines thresholds
├── weather.py            # Weather fetching logic and alert workflow
├── stock.py              # Stock price + news fetching and alert workflow
├── email_utils.py        # Reusable email sending function
├── utils.py              # Shared error logging utility
├── main.py               # Entry point — routes user to weather or stock workflow
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/automation-projects.git
cd automation-projects/multi_api_alert_bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project directory:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_TO=receiver_email@gmail.com

WEATHER_API_KEY=your_openweathermap_api_key
STOCK_ENDPOINT=https://www.alphavantage.co/query
STOCK_API_KEY=your_alphavantage_api_key
NEWS_API_KEY=your_newsapi_key
```

⚠️ Use a Gmail App Password, not your actual Gmail password.

### 4. Run the script

```bash
python main.py
```

---

## 🖥️ Example Output

```
1. Weather Alert
2. Stock Alert
Choose (1/2): 1
Enter city: London
⚠️ WEATHER ALERT

📍 Location: London
🌡️ Temperature: 8°C
☁️ Condition: Overcast Clouds

🚨 Reason: Temperature dropped below 10°C (8°C)
🕒 Time: 2026-04-20 15:03:18

🧣 Brrr! It's cold out there. Wear a jacket.
📧 Email sent successfully!
```

```
1. Weather Alert
2. Stock Alert
Choose (1/2): 2
Enter the stock symbol (e.g. AAPL, TSLA, BTC): AAPL
Do you want to send info about AAPL to your email? (YES/NO): YES
📧 Email sent successfully!
```

---

## 🤖 Alert Logic

### Weather Alerts

| Condition | Threshold | Advice |
|---|---|---|
| Rain or drizzle | Any | ☔ Grab an umbrella! |
| Cold temperature | Below 10°C | 🧣 Wear a jacket |
| High temperature | Above 30°C | 💧 Stay hydrated |

### Stock Alerts

| Trigger | Action |
|---|---|
| Price change ≥ 5% | Sends stock alert email automatically |
| User opts in (YES) | Sends stock alert email regardless of change |
| Email includes | Symbol, % change, price, and top 3 news headlines |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `requests` | Fetch data from weather, stock, and news APIs |
| `python-dotenv` | Securely load credentials from `.env` |
| `smtplib` | Send emails via SMTP |
| `email` | Format structured email messages |

---

## 🔒 Security Notes

- **Never commit `.env` to GitHub.** Add it to your `.gitignore`:

```
.env
error.log
```

- **Always use an App Password** for Gmail SMTP authentication — never your real password.
- All API keys are loaded at runtime from environment variables via `config.py`.

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

A production-style Python automation tool that integrates three real-world APIs to monitor
weather and stock conditions, and delivers intelligent email alerts — demonstrating modular
architecture, threshold-based logic, and scalable automation design.
