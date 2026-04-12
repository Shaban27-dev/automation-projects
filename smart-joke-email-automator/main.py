import requests
import json
import os
import time
import smtplib
import random
from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv

# ---------------------------- CONFIG ------------------------------- #
path = r"C:\Users\Lenovo\classroom\automation-projects\smart-joke-email-automator\.env"

load_dotenv(dotenv_path=path)

BASE_DIR = os.getcwd()
joke_file = r"C:\Users\Lenovo\classroom\automation-projects\smart-joke-email-automator\daily_joke.json"

MY_EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASS")
RECIPIENT_EMAIL = os.getenv("EMAIL_TO")


# ---------------------------- FETCH JOKE ------------------------------- #
def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    for attempt in range(3):
        try:
            print(f"🌐 Attempt {attempt + 1}: Fetching joke...")
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            data = response.json()

            return {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "setup": data.get("setup", ""),
                "punchline": data.get("punchline", "")
            }

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error: {e}")
            time.sleep(2)

    return {"error": "Failed to fetch joke"}


# ---------------------------- SAVE DATA ------------------------------- #
def save_joke(entry):
    if "error" in entry:
        print("❌ Joke not saved.")
        return

    try:
        if os.path.exists(joke_file):
            with open(joke_file, "r", encoding="utf-8") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = []
        else:
            history = []

        history.append(entry)
        history = history[-50:]  # limit size

        with open(joke_file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)

        print("✅ Joke saved successfully.")

    except Exception as e:
        print(f"❌ File error: {e}")


# ---------------------------- EMAIL SENDER ----------------------------- #
def send_email():
    if datetime.now().weekday() != 6:
        print("🗓️ Not Sunday. Skipping email.")
        return

    try:
        if not os.path.exists(joke_file):
            print("❌ No joke history found.")
            return

        with open(joke_file, "r", encoding="utf-8") as f:
            jokes = json.load(f)

        if not jokes:
            print("❌ No jokes available.")
            return

        joke = random.choice(jokes)

        msg = EmailMessage()
        msg["Subject"] = "Sunday Joke ☀️"
        msg["From"] = MY_EMAIL
        msg["To"] = RECIPIENT_EMAIL

        msg.set_content(
            f"""
Hello,

Here’s your Sunday joke 😄

{joke.get("setup")}
...
{joke.get("punchline")}

Have a great day!
"""
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(MY_EMAIL, PASSWORD)
            smtp.send_message(msg)

        print("📧 Email sent successfully!")

    except json.JSONDecodeError:
        print("❌ Corrupted JSON file.")
    except smtplib.SMTPException as e:
        print(f"❌ Email error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# ---------------------------- MAIN ------------------------------- #
def main():
    print("===== Joke Automation System =====")

    joke = fetch_joke()
    save_joke(joke)
    send_email()


# ---------------------------- RUN ------------------------------- #
if __name__ == "__main__":
    main()