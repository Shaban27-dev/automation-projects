# 🌦️ Weather API Fetcher

A smart command-line weather assistant built with Python that fetches real-time weather data, gives contextual advice, and keeps a local history of your queries.

---

## ✨ Features

- 🌐 Fetches live weather data using the [OpenWeatherMap API](https://openweathermap.org/api)
- 🤖 Provides smart contextual advice based on temperature and conditions (rain, cold, heat)
- 📝 Logs every query to a local JSON history file (capped at 50 entries)
- 🛡️ Handles errors gracefully:
  - Invalid API key  
  - City not found  
  - Network failures  
- ⚡ Fast, lightweight CLI tool with no heavy dependencies

---

## 💼 Real-World Use Cases

- Build weather-based automation systems  
- Integrate into alert systems (rain, heat warnings)  
- Use as a base for dashboards or monitoring tools  
- Extend into email/SMS notification systems  

---

## 🧠 Skills Demonstrated

- API integration using `requests`  
- Environment variable management (`python-dotenv`)  
- JSON data storage and logging  
- Robust error handling and validation  
- Clean and modular Python code structure  

---

## 📁 Project Structure

```
weather-api-fetcher/
├── API.env                 # Stores your OpenWeatherMap API key (not committed to Git)
├── main.py                 # Main application script
├── weather_history.json    # Auto-generated query history log
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/automation-projects.git
cd automation-projects/weather-api-fetcher
```

### 2. Install dependencies

```bash
pip install requests python-dotenv
```

### 3. Set up your API key

Create a file named `API.env` in the project directory:

```
WEATHER_API_KEY=your_openweathermap_api_key_here
```

> Get a free API key at [https://openweathermap.org/api](https://openweathermap.org/api)

### 4. Run the script

```bash
python main.py
```

You'll be prompted to enter a city name, and the assistant will return current weather data along with a helpful tip.

---

## 🖥️ Example Output

```
===== Weather Assistant =====
Which city would you like to check? London
🌐 Connecting to OpenWeather for: London...
✅ Logged: London at 8°C
🤖 Assistant: 🧣 Brrr! It's cold out there. Wear a jacket.
```

---

## 🤖 Assistant Logic

| Condition | Advice |
|---|---|
| Rain or drizzle detected | ☔ Grab an umbrella! |
| Temperature below 10°C | 🧣 Wear a jacket |
| Temperature above 30°C | 💧 Stay hydrated |
| Everything else | 😊 Enjoy your day! |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `requests` | Makes HTTP calls to the OpenWeatherMap API |
| `python-dotenv` | Loads the API key securely from `API.env` |

---

## 🔒 Security Notes

- **Never commit `API.env` to GitHub.** Add it to your `.gitignore`:

```
API.env
weather_history.json
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).


## 👨‍💻 Author

Shaban Alam
📧 shabandev27@gmail.com

Python Developer focused on automation, APIs, and data tools.
Available for freelance work — building scripts, automation systems, and custom tools.

📌 Summary

A production-style Python script demonstrating API usage, error handling,
and data logging — ready to be extended into real-world automation systems.