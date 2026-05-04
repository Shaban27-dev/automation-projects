import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def _build_html(jobs: list[dict]) -> str:
    rows = ""
    for job in jobs:
        rows += f"""
        <tr>
          <td style="padding:10px 12px;border-bottom:1px solid #eee;">
            <a href="{job['url']}" style="font-weight:600;color:#2563eb;text-decoration:none;">{job['title']}</a>
            <div style="font-size:13px;color:#555;margin-top:2px;">{job['company']}</div>
          </td>
          <td style="padding:10px 12px;border-bottom:1px solid #eee;font-size:13px;color:#444;">{job.get('salary','N/A')}</td>
          <td style="padding:10px 12px;border-bottom:1px solid #eee;font-size:12px;color:#666;">{job.get('tags','')}</td>
        </tr>"""

    return f"""
    <html><body style="font-family:sans-serif;max-width:680px;margin:0 auto;color:#111;">
      <h2 style="font-size:18px;font-weight:600;margin-bottom:4px;">Job Alert — {len(jobs)} new listing{'s' if len(jobs)!=1 else ''}</h2>
      <p style="font-size:13px;color:#666;margin-top:0;">{datetime.now().strftime('%A, %d %B %Y · %H:%M')}</p>
      <table style="width:100%;border-collapse:collapse;font-size:14px;">
        <thead>
          <tr style="background:#f5f5f5;">
            <th style="padding:10px 12px;text-align:left;font-weight:500;">Role</th>
            <th style="padding:10px 12px;text-align:left;font-weight:500;">Salary</th>
            <th style="padding:10px 12px;text-align:left;font-weight:500;">Tags</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
      <p style="font-size:12px;color:#999;margin-top:20px;">Sent by Job Alert Automator · All jobs also logged to Google Sheets</p>
    </body></html>"""


def send_digest(jobs: list[dict], sender: str, password: str, recipient: str) -> bool:
    """Send an HTML digest email. Returns True on success."""
    if not jobs:
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"[Job Alert] {len(jobs)} new listing{'s' if len(jobs)!=1 else ''} — {datetime.now().strftime('%d %b %Y')}"
    msg["From"] = sender
    msg["To"] = recipient

    plain = "\n".join(
        f"- {j['title']} @ {j['company']} | {j.get('salary','N/A')} | {j['url']}"
        for j in jobs
    )
    msg.attach(MIMEText(plain, "plain"))
    msg.attach(MIMEText(_build_html(jobs), "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, recipient, msg.as_string())
        return True
    except smtplib.SMTPAuthenticationError:
        print("  ERROR: Gmail authentication failed. Check EMAIL_PASSWORD in .env.")
        print("  You need a Gmail App Password — see README for setup instructions.")
        return False
    except Exception as e:
        print(f"  ERROR sending email: {e}")
        return False
