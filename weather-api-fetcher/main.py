import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# ---------------------------- CONFIG ------------------------------- #
path = r"C:\Users\Lenovo\classroom\automation-projects\weather-api-fetcher\API.env"
history_file = r"C:\Users\Lenovo\classroom\automation-projects\weather-api-fetcher\weather_history.json"
MAX_HISTORY = 50

load_dotenv(dotenv_path=path)

API_KEY = os.getenv("WEATHER_API_KEY")


# ---------------------------- FETCH WEATHER ------------------------------- #
def fetch_weather(city):
    if not API_KEY:
        return {"error": "API Key missing."}

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        print(f"🌐 Connecting to OpenWeather for: {city}...")

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        
        # --- SAFE DATA EXTRACTION ---
        condition = data.get("weather", [{}])[0].get("description", "").lower()
        temp = data.get("main", {}).get("temp", 0)

        # --- SMART ASSISTANT LOGIC ---
        advice = "Enjoy your day!" # Default advice
        
        if "rain" in condition or "drizzle" in condition:
            advice = "☔ Grab an umbrella! It looks like rain."
        elif temp < 10:
            advice = "🧣 Brrr! It's cold out there. Wear a jacket."
        elif temp > 30:
            advice = "💧 Stay hydrated! It's a hot one."
        
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "city": data.get("name"),
            "temp": temp,
            "condition": condition,
            "assistant_advice": advice
        }
    
    except requests.exceptions.HTTPError as http_err:
        status_code = http_err.response.status_code if http_err.response else None

        if status_code == 401:
            return {"error": "Invalid API Key."}
        elif status_code == 404:
            return {"error": "City not found."}

        return {"error": f"HTTP error: {http_err}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}

    # JSON decode safeguard 
    except ValueError:
        return {"error": "Invalid response format (JSON decode failed)."}


# ---------------------------- HISTORY LOGGER ------------------------------- #
def history_logger(new_entry):
    if "error" in new_entry:
        print(f"❌ Cannot log: {new_entry['error']}")
        return

    # --- HISTORY LOGGER LOGIC ---
    # Load existing data if it exists
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError: # Handle empty or broken files
                history = []
    else:
        history = []

    # Append the new entry to the list
    history.append(new_entry)

    # Limit history size
    history = history[-MAX_HISTORY:]

    # Save the entire updated list back to the file
    try:
        with open(history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Logged: {new_entry['city']} at {new_entry['temp']}°C")
        print(f"🤖 Assistant: {new_entry['assistant_advice']}")

    except Exception as e:
        print(f"❌ Failed to save history: {e}")


# ---------------------------- MAIN ------------------------------- #
def main():
    print("===== Weather Assistant =====")

    city = input("Which city would you like to check? ").strip()

    if not city:
        print("❌ City cannot be empty.")
        return
    
    weather_data = fetch_weather(city)

    if "error" in weather_data:
        print(f"❌ {weather_data['error']}")
        return
    
    history_logger(weather_data)


# ---------------------------- RUN ------------------------------- #
if __name__ == "__main__":
    main()
