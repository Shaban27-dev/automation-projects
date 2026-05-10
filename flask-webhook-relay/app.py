import os
import json
import logging
from datetime import datetime
from functools import wraps

from flask import Flask, request, jsonify
from dotenv import load_dotenv

from notifier import send_alert

ENV_PATH = r"C:\Users\Lenovo\classroom\automation-projects\flask-webhook-relay\.env"
load_dotenv(ENV_PATH)

# ── Logging ─────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("webhook.log", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)

# ── Config ──────────────────────────────────────────────────────────────────────
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "")
EMAIL_SENDER   = os.getenv("EMAIL_SENDER")
EMAIL_PASS     = os.getenv("EMAIL_PASSWORD")
EMAIL_TO       = os.getenv("EMAIL_RECIPIENT")
PORT           = int(os.getenv("FLASK_PORT", 5000))
DEBUG          = os.getenv("FLASK_DEBUG", "false").lower() == "true"

app = Flask(__name__)

# ── Auth decorator ──────────────────────────────────────────────────────────────

def require_token(f):
    """Decorator: reject any request missing or providing the wrong secret token.

    Accepts the token in either:
      - Header:  X-Webhook-Secret: <token>
      - Body:    { "secret": "<token>", ... }

    This mirrors how n8n sends auth — you can configure either method in
    n8n's webhook node under "Authentication → Header Auth".
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        if not WEBHOOK_SECRET:
            log.warning("WEBHOOK_SECRET not set — running without auth (dev only)")
            return f(*args, **kwargs)

        # Check header first, then fall back to body field
        token = request.headers.get("X-Webhook-Secret")
        if not token:
            body = request.get_json(silent=True) or {}
            token = body.get("secret")

        if token != WEBHOOK_SECRET:
            log.warning(f"Rejected request — bad or missing token from {request.remote_addr}")
            return jsonify({"error": "Unauthorised"}), 401

        return f(*args, **kwargs)
    return decorated

# ── Helpers ─────────────────────────────────────────────────────────────────────

def print_payload(payload: dict, source: str = "unknown"):
    """Pretty-print a payload to the terminal — structured and readable."""
    width = 52
    print("\n" + "─" * width)
    print(f"  Webhook received · {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Source: {source}")
    print("─" * width)
    for key, value in payload.items():
        if key == "secret":
            continue  # never echo the secret token
        v = json.dumps(value) if isinstance(value, (dict, list)) else str(value)
        print(f"  {key:<20} {v}")
    print("─" * width + "\n")


def build_email_subject(payload: dict) -> str:
    """Build a meaningful email subject from common payload fields."""
    event     = payload.get("event", "")
    source    = payload.get("source", "webhook")
    status    = payload.get("status", "")
    name      = payload.get("name", payload.get("title", ""))

    parts = ["[Webhook Alert]", source]
    if event:
        parts.append(event)
    if name:
        parts.append(f"— {name}")
    if status:
        parts.append(f"({status})")

    return " ".join(parts)

# ── Routes ───────────────────────────────────────────────────────────────────────

@app.route("/webhook", methods=["POST"])
@require_token
def webhook():
    """Main webhook endpoint.

    Expects a JSON body. On success:
      1. Prints structured payload to terminal
      2. Sends a Gmail HTML alert
      3. Returns { "status": "ok", "received": <int> } with 200

    Compatible with n8n's Webhook node — point it at:
      http://<your-ngrok-url>/webhook
    and set Header Auth: X-Webhook-Secret = <your token>
    """
    payload = request.get_json(silent=True)

    if not payload:
        log.warning("Empty or non-JSON body received")
        return jsonify({"error": "Expected JSON body"}), 400

    source = payload.get("source", request.headers.get("User-Agent", "unknown"))
    log.info(f"Payload received from '{source}' with {len(payload)} field(s)")

    # 1 — Print to terminal
    print_payload(payload, source=source)

    # 2 — Send email
    email_payload = {k: v for k, v in payload.items() if k != "secret"}
    subject = build_email_subject(payload)

    if EMAIL_SENDER and EMAIL_PASS and EMAIL_TO:
        success = send_alert(subject, email_payload, EMAIL_SENDER, EMAIL_PASS, EMAIL_TO)
        if success:
            log.info(f"Email alert sent → {EMAIL_TO}")
        email_status = "sent" if success else "failed"
    else:
        log.warning("Email credentials not set — skipping alert")
        email_status = "skipped"

    return jsonify({
        "status":  "ok",
        "received": len(email_payload),
        "email":   email_status,
    }), 200


@app.route("/health", methods=["GET"])
def health():
    """Health check — useful for confirming ngrok tunnel is live."""
    return jsonify({
        "status":    "running",
        "timestamp": datetime.now().isoformat(),
        "auth":      "enabled" if WEBHOOK_SECRET else "disabled (dev mode)",
    }), 200


@app.route("/test", methods=["GET"])
def test_ui():
    """Browser-friendly test form — fire a test payload without Postman."""
    secret_hint = "configured" if WEBHOOK_SECRET else "NOT SET"
    return f"""<!DOCTYPE html>
<html>
<head>
  <title>Webhook Tester</title>
  <style>
    body {{ font-family: sans-serif; max-width: 560px; margin: 60px auto; color: #222; }}
    h2   {{ font-weight: 500; margin-bottom: 4px; }}
    p    {{ font-size: 13px; color: #777; margin-top: 0; }}
    textarea {{ width: 100%; height: 160px; font-family: monospace; font-size: 13px;
                border: 1px solid #ddd; border-radius: 6px; padding: 10px; box-sizing: border-box; }}
    button {{ margin-top: 10px; padding: 9px 20px; background: #2563eb; color: #fff;
              border: none; border-radius: 6px; cursor: pointer; font-size: 14px; }}
    button:hover {{ background: #1d4ed8; }}
    pre  {{ background: #f5f5f5; border-radius: 6px; padding: 12px; font-size: 13px;
            white-space: pre-wrap; margin-top: 16px; }}
    .badge {{ display:inline-block; padding:2px 8px; border-radius:4px; font-size:11px;
              background:#e8f5e9; color:#2e7d32; font-weight:500; }}
  </style>
</head>
<body>
  <h2>Webhook Tester</h2>
  <p>Auth: <span class="badge">{secret_hint}</span> &nbsp;·&nbsp;
     Send a POST to <code>/webhook</code></p>
  <textarea id="body">{{
  "source": "test-ui",
  "event": "test_fired",
  "name": "My test payload",
  "status": "success",
  "value": 42
}}</textarea>
  <br>
  <button onclick="fire()">Fire webhook</button>
  <pre id="out">Response will appear here…</pre>
  <script>
    async function fire() {{
      const body = JSON.parse(document.getElementById('body').value);
      body.secret = "{WEBHOOK_SECRET}";
      const r = await fetch('/webhook', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify(body)
      }});
      const data = await r.json();
      document.getElementById('out').textContent =
        'Status: ' + r.status + '\\n\\n' + JSON.stringify(data, null, 2);
    }}
  </script>
</body>
</html>""", 200


# ── Entry point ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 52)
    print("  Flask Webhook Server")
    print("=" * 52)
    print(f"  Auth   : {'✓ token required' if WEBHOOK_SECRET else '✗ DISABLED (set WEBHOOK_SECRET)'}")
    print(f"  Email  : {'✓ configured' if EMAIL_SENDER else '✗ not set'}")
    print(f"  Port   : {PORT}")
    print("=" * 52)
    print(f"\n  Endpoints:")
    print(f"    POST /webhook  ← main trigger")
    print(f"    GET  /health   ← liveness check")
    print(f"    GET  /test     ← browser test form")
    print(f"\n  To expose to n8n:")
    print(f"    ngrok http {PORT}")
    print(f"    Then use the ngrok URL in your n8n Webhook node\n")
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
