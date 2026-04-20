import requests
from datetime import datetime
from config import WEATHER_API_KEY, TEMP_THRESHOLD
from email_utils import send_email
from utils import log_error


def fetch_weather(city):
    try:
        if not city:
            raise ValueError("City cannot be empty")

        url = f"https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        condition = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]

        advice = "Enjoy your day!" # Default advice
        alert_needed = False
        reason = ""
        
        if "rain" in condition or "drizzle" in condition:
            advice = "☔ Grab an umbrella! It looks like rain."
            alert_needed = True
            reason = "Precipitation detected (Rain/Drizzle)"
        elif temp < 10:
            advice = "🧣 Brrr! It's cold out there. Wear a jacket."
            alert_needed = True
            reason = f"Temperature dropped below 10°C ({temp}°C)"
        elif temp > 30:
            advice = "💧 Stay hydrated! It's a hot one."
            alert_needed = True
            reason = f"Temperature exceeded threshold ({TEMP_THRESHOLD}°C)"

        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "city": data.get("name"),
            "temp": temp,
            "condition": condition,
            "assistant_advice": advice,
            "alert_needed": alert_needed,
            "reason": reason
        }

    except requests.exceptions.Timeout:
        print("⏳ Request timed out. Try again.")
    except requests.exceptions.HTTPError as e:
        log_error(e)
        if e.response.status_code == 404:
            print("❌ City not found.")
        elif e.response.status_code == 401:
            print("❌ Invalid API key.")
        else:
            print(f"❌ HTTP error: {e}")
    except requests.exceptions.RequestException:
        print("❌ Network error. Check internet connection.")
    except KeyError:
        print("❌ Unexpected API response format.")
    except ValueError as e:
        log_error(e)
        print(f"❌ {e}")

    return None


def weather_workflow():
    city = input("Enter city: ").strip()
    data = fetch_weather(city)

    if data["alert_needed"]:
        message = f"""
    ⚠️ WEATHER ALERT

    📍 Location: {data.get('city', 'Unknown')}
    🌡️ Temperature: {data.get('temp', 'N/A')}°C
    ☁️ Condition: {data.get('condition', 'N/A')}

    🚨 Reason: {data.get('reason', 'Not specified')}
    🕒 Time: {data.get('timestamp', 'N/A')}

    {data.get('assistant_advice', '')}
    """
        send_email("Weather Alert", message)
    else:
        print(f"No alert needed. Current temp: {data['temp']}°C")
    