import requests
from config import STOCK_API_KEY, NEWS_API_KEY, STOCK_ENDPOINT, STOCK_THRESHOLD
from email_utils import send_email
from utils import log_error


def get_stock(symbol):
    try:
        if not symbol:
            raise ValueError("Stock symbol cannot be empty")
        
        parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": STOCK_API_KEY,
        }
        response = requests.get(STOCK_ENDPOINT, params=parameters)
        response.raise_for_status()
        data = response.json()

        if "Note" in data:
            print(f"⚠️ API Limit Reached: {data['Note']}")
            return None
        elif "Error Message" in data:
            print(f"❌ Invalid Symbol: {data['Error Message']}")
            return None
        
        if "Time Series (Daily)" not in data:
            print("❌ Unknown Error. Full response:", data)
            return None

        # Get the last two days of closing prices
        time_series = data["Time Series (Daily)"]
        dates = list(time_series.keys())
        
        yesterday_close = float(time_series[dates[0]]["4. close"])
        day_before_close = float(time_series[dates[1]]["4. close"])

        diff = yesterday_close - day_before_close
        percentage_diff = (diff / day_before_close) * 100
        
        # Determine the emoji for the subject line
        up_down = "🔺" if diff > 0 else "🔻"
        
        return {
            "symbol": symbol,
            "perc": round(percentage_diff, 2),
            "direction": up_down,
            "yesterday": yesterday_close
        }

    except requests.exceptions.Timeout:
        print("⏳ Stock API timeout.")
    except requests.exceptions.RequestException:
        print("❌ Network error.")
    except (KeyError, IndexError):
        print("❌ Unexpected stock data format.")
    except ValueError as e:
        log_error(e)
        print(f"❌ {e}")

    return None


def get_news(symbol):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": symbol, 
        "apiKey": NEWS_API_KEY, 
        "pageSize": 3
        }

    response = requests.get(url, params=params)
    response.raise_for_status()
    articles = response.json().get("articles", [])

    return [(a["title"], a["description"]) for a in articles]


def stock_workflow():
    symbol = input("Enter the stock symbol (e.g. AAPL, TSLA, BTC): ").upper()
    track = input(f"Do you want to info about {symbol} to your email? (YES/NO): ").upper()

    result = get_stock(symbol)
    if result is None:
        print("⚠️ Could not retrieve stock data. Skipping alert.")
        return

    change = result["perc"]
    price = result["yesterday"]
    direction = result["direction"]

    if abs(change) >= STOCK_THRESHOLD or track == "YES":
        news = get_news(symbol)

        news_text = "\n\n".join(
    [f"Title: {t}\nBrief: {d if d else 'No description available.'}" for t, d in news]
    )


        message = f"""
📉 STOCK ALERT

{symbol} moved {direction}{change:.2f}%
Price: ${price}

📰 News:
{news_text}
"""
        send_email("Stock Alert", message)
    else:
        print("No significant movement.")