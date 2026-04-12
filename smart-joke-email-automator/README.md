# 😂 Smart Joke Email Automator

A smart Python automation tool that fetches jokes from an online API, stores them locally, and sends a random joke via email automatically (every Sunday), combining API integration, data persistence, and email automation.

---

## ✨ Features

- 🌐 Fetches random jokes using the Official Joke API
- 📝 Stores jokes locally in a JSON file (with history tracking)
- 📧 Automatically sends a random joke via email (Sunday trigger)
- 🔁 Retry logic for handling API failures
- 🛡️ Handles errors gracefully:
- API request failures
- Corrupted or empty JSON files
- Email sending issues
- ⚡ Lightweight CLI automation script with clean structure

---

## 💼 Real-World Use Cases

- Automate email notifications (reports, alerts, updates)
- Build scheduled content delivery systems
- Use as a base for newsletter automation tools
- Extend into daily motivational/email bots
- Integrate with cron jobs or task schedulers

---

## 🧠 Skills Demonstrated

- API integration using requests
- Email automation using smtplib and EmailMessage
- Environment variable management (python-dotenv)
- JSON data storage and file handling
- Retry logic and robust error handling
- Clean modular Python scripting

---

## 📁 Project Structure

```
smart-joke-email-automator/
├── .env                  # Stores email credentials (not committed to Git)
├── main.py               # Main automation script
├── daily_joke.json       # Auto-generated joke history
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/automation-projects.git
cd automation-projects/smart-joke-email-automator
```

### 2. Install dependencies

```bash
pip install requests python-dotenv
```

### 3. Set up environment variables

Create a .env file in the project directory:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_TO=receiver_email@gmail.com
```

⚠️ Use a Gmail App Password, not your actual password.

### 4. Run the script

```bash
python main.py
```

---

## 🖥️ Example Output

```
===== Joke Automation System =====
🌐 Attempt 1: Fetching joke...
✅ Joke saved successfully.
📧 Email sent successfully!

(If not Sunday)

🗓️ Not Sunday. Skipping email.
```

---

## 🤖 Automation Logic

| Step	 | Action |
|---|---|
| Fetch | Retrieves a random joke from API |
| Store | Saves joke in local JSON history |
| Select | Picks a random joke from history |
| Send |Emails joke if it's Sunday |

---

## 📦 Dependencies

| Package | Purpose
|---|---|
| `requests` | Fetch jokes from API |
| `python-dotenv` | Securely load email credentials |
| `smtplib` |	Send emails via SMTP |
| `email` | Format structured email messages |

---

## 🔒 Security Notes

- **Never commit `API.env` to GitHub.** Add it to your `.gitignore`:

```
Add this to your .gitignore:
.env
daily_joke.json
```

- **Always use `App Password` for email authentication

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).


## 👨‍💻 Author

Shaban Alam
📧 shabandev27@gmail.com

Python Developer focused on automation, APIs, and data tools.
Available for freelance work — building scripts, automation systems, and custom tools.

📌 Summary

A production-style Python automation tool that combines API data fetching, local storage, and scheduled email delivery — demonstrating real-world automation skills and scalable design.