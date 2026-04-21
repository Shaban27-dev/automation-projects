# automation-projects

A collection of Python automation projects — API integrations, email automation,
and smart CLI tools built for real-world use cases.

📧 shabandev27@gmail.com · Open to freelance Python work

---

## Projects

### Multi-API Alert Bot
Monitors live weather conditions and stock market movements across three APIs.
Sends formatted email alerts with contextual advice and related news headlines
when thresholds are exceeded. Modular architecture with shared config and error logging.
→ `multi_api_alert_bot/`

### Smart Joke Email Automator
Fetches a random joke from a public API and sends it automatically via email.
Handles SMTP authentication, formats the message, and delivers with zero manual input.
→ `smart-joke-email-automator/`

### Weather API Fetcher
Connects to the OpenWeatherMap API to retrieve live weather data for any city.
Gives smart contextual advice based on temperature and conditions, and logs
every query to a local JSON history file.
→ `weather-api-fetcher/`

---

## Stack

Python 3 · Requests · smtplib · python-dotenv · JSON · OpenWeatherMap API · Alpha Vantage API · NewsAPI

## What these projects demonstrate

- Multi-API integration using `requests` with real-world endpoints
- Secure credential management with `.env` files and `python-dotenv`
- Email automation via `smtplib` and SMTP authentication
- Threshold-based alert logic and conditional email triggers
- Smart assistant logic — condition-based responses and advice
- Persistent local data storage using JSON read/write cycles
- Robust error handling — HTTP errors, bad input, network failures, API rate limits
- Modular project structure with shared config and utility modules
- Clean CLI design with input validation and formatted output

---

## Run any project

Each project folder contains its own `README.md` with setup and run instructions.
All projects require Python 3 and a small set of pip dependencies.

```bash
cd multi_api_alert_bot
python main.py
```

---

## Available for freelance work

I build Python automation scripts, API integrations, email tools, and CLI
applications. If you have a repetitive task that Python can handle — I can
build it.

📧 shabandev27@gmail.com
