# 🔗 Flask Webhook Relay

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![n8n Compatible](https://img.shields.io/badge/n8n-Compatible-orange)

A production-ready Flask server that receives incoming webhook payloads, authenticates
them via a secret token, prints structured logs to the terminal, and immediately fires
a formatted HTML email alert — bridging any external automation tool (n8n, Zapier,
GitHub Actions) to your inbox with zero manual effort.

---

## ✨ Features

- 🌐 Accepts `POST /webhook` from any source — n8n, Zapier, GitHub, custom scripts
- 🔐 Token authentication via `X-Webhook-Secret` header or request body field
- 📧 Sends a polished HTML email alert for every valid webhook received
- 🖥️ Structured terminal output — timestamped, readable, never cluttered
- 📋 Writes a persistent `webhook.log` file for full audit trail and debugging
- 🩺 `GET /health` endpoint — confirm the server is live before connecting a tool
- 🧪 `GET /test` — browser-friendly test UI to fire payloads without Postman
- 🧠 Smart email subject builder — assembles meaningful subjects from payload fields
- 🛡️ Handles errors gracefully:
  - Missing or malformed JSON body
  - Unauthorised requests (wrong or absent token)
  - SMTP authentication failures
  - Missing email credentials (graceful skip with log warning)
- ⚡ Modular design — `app.py` handles routing, `notifier.py` owns all email logic

---

## ⏳ Time Saved / Business Value

Without this tool, monitoring incoming webhooks means logging into dashboards,
manually reading payloads, formatting alerts, and forwarding summaries by hand.

| Task | Manual Approach | With This Tool |
|---|---|---|
| Read incoming webhook payload | Open dashboard, parse JSON manually | Instant — structured terminal log |
| Format and send alert email | Write email, copy-paste fields, send | Automatic HTML email on every hit |
| Audit webhook history | No persistent record | `webhook.log` captures every event |
| Test new webhook sources | Postman or curl required | Built-in `/test` UI in the browser |
| Secure the endpoint | Manual IP filtering or none | Token auth out of the box |

**Business value:** Any developer or agency running n8n, Zapier, or custom integrations
can point their webhook triggers at this server and receive instant, formatted email
notifications — no dashboard, no manual checks, no missed events. The `/test` UI
and `/health` endpoint mean it can be validated and handed off to a client in minutes.

---

## 💼 Real-World Use Cases

- Receive n8n or Zapier workflow triggers and get emailed the payload instantly
- Monitor GitHub webhooks (push, PR, deploy) and alert your team by email
- Build a lightweight alerting layer for any API that supports outbound webhooks
- Replace expensive third-party notification services with a self-hosted relay
- Use as a backend for form submissions, payment confirmations, or CRM triggers
- Prototype webhook integrations locally using ngrok before deploying to a server

---

## 🧠 Skills Demonstrated

- Flask web server — routing, request handling, JSON parsing, response formatting
- Python decorators — `@require_token` auth middleware wrapping protected routes
- Token-based authentication — header-first with body fallback, mirrors n8n auth flow
- HTML email composition — inline CSS, dynamic table rows, `MIMEMultipart` structure
- Gmail SMTP delivery via `smtplib` with `SMTP_SSL` and App Password authentication
- Structured logging with Python's `logging` module (console + persistent file handler)
- Dynamic email subject generation from arbitrary payload fields
- Environment variable management with `python-dotenv`
- Clean separation of concerns — routing in `app.py`, email in `notifier.py`
- Built-in browser test UI — served as raw HTML from a Flask route, no templates needed
- Defensive error handling at every integration point (auth, JSON, SMTP)

---

## 📁 Project Structure

```
flask-webhook-relay/
├── assets/
│   ├── email-result.png      # Screenshot — example HTML email received
│   ├── ngrok-tunnel.png      # Screenshot — ngrok tunnel active
│   ├── server-logs.png       # Screenshot — structured terminal output
│   └── tester-ui.png         # Screenshot — /test browser UI
├── .env                      # Email credentials and webhook secret (not committed to Git)
├── .gitignore
├── app.py                    # Flask server — routes, auth decorator, helpers
├── notifier.py               # HTML email builder and SMTP sender
├── requirements.txt
├── webhook.log               # Auto-generated audit log (not committed to Git)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/automation-projects.git
cd automation-projects/flask-webhook-relay
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up a Gmail App Password

Google requires an App Password for SMTP — not your main Gmail password:

1. Enable 2-Step Verification on your Google account
2. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Create an app password → copy the 16-character code

### 4. Set up environment variables

Create a `.env` file in the project directory:

```
WEBHOOK_SECRET=your_secret_token_here
EMAIL_SENDER=your_gmail@gmail.com
EMAIL_PASSWORD=your_16_char_app_password
EMAIL_RECIPIENT=your_gmail@gmail.com
FLASK_PORT=5000
FLASK_DEBUG=false
```

### 5. Run the server

```bash
python app.py
```

### 6. Expose to n8n or external tools (optional)

Use [ngrok](https://ngrok.com) to create a public tunnel to your local server:

```bash
ngrok http 5000
```

Then paste the ngrok URL into your n8n Webhook node and set:
- **HTTP Method:** POST
- **Header Auth:** `X-Webhook-Secret` → `your_secret_token_here`

---

## 🖥️ Example Output

**Terminal logs on startup:**
```
====================================================
  Flask Webhook Server
====================================================
  Auth   : ✓ token required
  Email  : ✓ configured
  Port   : 5000
====================================================

  Endpoints:
    POST /webhook  ← main trigger
    GET  /health   ← liveness check
    GET  /test     ← browser test form

  To expose to n8n:
    ngrok http 5000
    Then use the ngrok URL in your n8n Webhook node
```

**Terminal logs on incoming webhook:**
```
────────────────────────────────────────────────────
  Webhook received · 2026-05-04 14:33:21
  Source: n8n-nodes-base.webhook
────────────────────────────────────────────────────
  event                test_fired
  name                 My test payload
  status               success
  value                42
────────────────────────────────────────────────────

2026-05-04 14:33:21 [INFO] Payload received from 'n8n' with 4 field(s)
2026-05-04 14:33:22 [INFO] Email alert sent → your_gmail@gmail.com
```

**`/health` endpoint response:**
```json
{
  "status": "running",
  "timestamp": "2026-05-04T14:33:00.123456",
  "auth": "enabled"
}
```

> 📸 Live screenshots of the test UI, terminal output, ngrok tunnel, and email result
> are available in the [`assets/`](./assets) folder.

---

## 🤖 Request Lifecycle

| Step | Action |
|---|---|
| Receive | Flask accepts `POST /webhook` — parses JSON body |
| Authenticate | `@require_token` checks `X-Webhook-Secret` header or body field |
| Log | Structured payload printed to terminal and appended to `webhook.log` |
| Build subject | `build_email_subject()` assembles a meaningful subject from payload fields |
| Notify | `notifier.py` builds HTML email and sends via Gmail SMTP |
| Respond | Returns `{ "status": "ok", "received": N, "email": "sent" }` with `200` |

---

## 🔀 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/webhook` | Main endpoint — accepts any JSON payload |
| `GET` | `/health` | Liveness check — confirms server is running |
| `GET` | `/test` | Browser UI — fire test payloads without Postman |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `flask` | Web server — routing, request handling, JSON responses |
| `python-dotenv` | Securely load config from `.env` |
| `smtplib` | Send HTML email alerts via Gmail SMTP |
| `email` (stdlib) | Build `MIMEMultipart` HTML email messages |
| `logging` (stdlib) | Structured console and file logging |
| `yagmail` | Simplified SMTP logic for sending clean HTML emails with one line of code |


---

## 🔒 Security Notes

- **Never commit `.env` to GitHub** — it contains your Gmail password and webhook secret:

```
.env
webhook.log
```

- `WEBHOOK_SECRET` guards the `/webhook` endpoint — any request with a missing or wrong
  token is rejected with `401 Unauthorised` and logged
- Always use a **Gmail App Password** for SMTP — never your real Google account password
- The `/test` UI embeds the secret token client-side — **only use in local/dev environments**,
  never expose this route on a public server without additional protection
- Set `FLASK_DEBUG=false` in any environment where the server is publicly accessible

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Shaban Alam**
📧 shabandev27@gmail.com
🐙 [github.com/Shaban27-dev](https://github.com/Shaban27-dev)

Python Developer focused on automation, APIs, and data tools.
Available for freelance work — building scripts, automation systems, and custom tools.

---

📌 **Summary**

A production-ready Flask webhook relay server that authenticates incoming requests,
logs structured payloads to the terminal and a persistent file, and immediately delivers
a formatted HTML email alert — demonstrating Flask routing, Python decorator-based
authentication, HTML email composition, structured logging, and modular design. Built
to integrate directly with n8n, Zapier, or any webhook-capable tool, and deployable
in minutes using ngrok for external access.
