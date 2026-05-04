import os
import json
import time
import logging
import schedule
import requests
from html import unescape
from datetime import datetime
from dotenv import load_dotenv

from sheets import log_jobs
from notifier import send_digest

# ── Logging setup ───────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("job_alert.log", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)

ENV_FILE = r"C:\Users\Lenovo\classroom\automation-projects\job-alert-automator\.env"
load_dotenv(ENV_FILE)

# ── Config ─────────────────────────────────────────────────────────────────────

KEYWORDS     = [k.strip().lower() for k in os.getenv("KEYWORDS", "python").split(",")]
TAGS         = [t.strip().lower() for t in os.getenv("TAGS", "python").split(",")]
MAX_RESULTS  = int(os.getenv("MAX_RESULTS", 20))
SHEET_ID     = os.getenv("SHEET_ID")
SHEET_NAME   = os.getenv("SHEET_NAME", "Job Listings")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASS   = os.getenv("EMAIL_PASSWORD")
EMAIL_TO     = os.getenv("EMAIL_RECIPIENT")
INTERVAL_HRS = int(os.getenv("RUN_INTERVAL_HOURS", 6))

SEEN_FILE    = "seen_jobs.json"
REMOTEOK_URL = "https://remoteok.com/api"

# ── Seen-job cache ──────────────────────────────────────────────────────────────

def load_seen() -> dict:
    """Load seen cache. Returns dict with 'ids' and 'fingerprints' sets."""
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE) as f:
            data = json.load(f)
            return {
                "ids":          set(data.get("ids", [])),
                "fingerprints": set(data.get("fingerprints", [])),
            }
    return {"ids": set(), "fingerprints": set()}


def save_seen(seen: dict):
    with open(SEEN_FILE, "w") as f:
        json.dump({
            "ids":          list(seen["ids"]),
            "fingerprints": list(seen["fingerprints"]),
        }, f, indent=2)

# ── Fetching & filtering ────────────────────────────────────────────────────────

def fetch_listings() -> list[dict]:
    """Fetch from RemoteOK API and return raw job dicts."""
    headers = {"User-Agent": "Mozilla/5.0 (job-alert-bot/1.0)"}
    try:
        resp = requests.get(REMOTEOK_URL, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        return [item for item in data if isinstance(item, dict) and item.get("id")]
    except requests.exceptions.Timeout:
        log.warning("Request timed out — will retry next cycle.")
        return []
    except requests.exceptions.HTTPError as e:
        log.warning(f"HTTP error from RemoteOK: {e}")
        return []
    except requests.exceptions.RequestException as e:
        log.error(f"Failed to fetch listings: {e}")
        return []


def matches(job: dict) -> bool:
    """Return True if the job matches any keyword or tag filter."""
    title    = job.get("position", "").lower()
    desc     = job.get("description", "").lower()
    job_tags = [t.lower() for t in job.get("tags", [])]

    keyword_match = any(kw in title or kw in desc for kw in KEYWORDS)
    tag_match     = any(tag in job_tags for tag in TAGS)
    return keyword_match or tag_match


def extract(job: dict) -> dict:
    """Normalise a raw RemoteOK job into a clean dict."""
    title   = unescape(job.get("position", "Unknown"))
    company = unescape(job.get("company", "Unknown"))
    tags    = ", ".join(job.get("tags", [])[:5])

    salary = ""
    if job.get("salary_min") and job.get("salary_max"):
        salary = f"${job['salary_min']:,} – ${job['salary_max']:,}"
    elif job.get("salary_min"):
        salary = f"${job['salary_min']:,}+"

    return {
        "id":          str(job["id"]),
        "fingerprint": f"{title.lower()}|{company.lower()}",  
        "title":       title,
        "company":     company,
        "tags":        tags,
        "salary":      salary or "N/A",
        "location":    job.get("location", "Remote"),
        "url":         job.get("url", f"https://remoteok.com/jobs/{job['id']}"),
        "date_found":  datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

# ── Main job ────────────────────────────────────────────────────────────────────

def run():
    log.info("Running job scan...")

    seen = load_seen()

    raw_listings = fetch_listings()
    log.info(f"Fetched {len(raw_listings)} total listings from RemoteOK")

    matched = [job for job in raw_listings if matches(job)]

    new_jobs = []
    for j in matched:
        candidate = extract(j)
        if candidate["id"] not in seen["ids"] and candidate["fingerprint"] not in seen["fingerprints"]:
            new_jobs.append(candidate)

    new_jobs = new_jobs[:MAX_RESULTS]
    log.info(f"Matched: {len(matched)} | New (unseen): {len(new_jobs)}")

    if not new_jobs:
        log.info("No new listings — nothing to log or send.")
        return

    for job in new_jobs:
        seen["ids"].add(job["id"])
        seen["fingerprints"].add(job["fingerprint"])
    save_seen(seen)

    # Log to Sheets
    if SHEET_ID:
        try:
            count = log_jobs(new_jobs, SHEET_ID, SHEET_NAME)
            log.info(f"Logged {count} rows to Google Sheets ✓")
        except Exception as e:
            log.error(f"Google Sheets logging failed: {e}")
    else:
        log.warning("SHEET_ID not set — skipping Sheets logging.")

    # Send email digest
    if EMAIL_SENDER and EMAIL_PASS and EMAIL_TO:
        success = send_digest(new_jobs, EMAIL_SENDER, EMAIL_PASS, EMAIL_TO)
        if success:
            log.info(f"Email digest sent to {EMAIL_TO} ✓")
    else:
        log.warning("Email credentials not set — skipping digest.")

    # Summary to terminal
    log.info("New listings:")
    for job in new_jobs:
        sal = f" | {job['salary']}" if job['salary'] != 'N/A' else ""
        log.info(f"  • {job['title']} @ {job['company']}{sal}")

# ── Entry point ─────────────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  Job Alert Automator")
    print("=" * 55)
    print(f"  Keywords : {', '.join(KEYWORDS)}")
    print(f"  Tags     : {', '.join(TAGS)}")
    print(f"  Interval : every {INTERVAL_HRS} hour(s)")
    print(f"  Sheet    : {'configured ✓' if SHEET_ID else 'NOT SET'}")
    print(f"  Email    : {'configured ✓' if EMAIL_SENDER else 'NOT SET'}")
    print("=" * 55)

    run()  # Run immediately on startup

    schedule.every(INTERVAL_HRS).hours.do(run)
    log.info(f"Scheduler active. Next run in {INTERVAL_HRS}h. Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
