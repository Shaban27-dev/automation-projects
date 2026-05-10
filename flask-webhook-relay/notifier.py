import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def _build_html(subject: str, payload: dict) -> str:
    rows = "".join(
        f"""<tr>
              <td style="padding:8px 12px;border-bottom:1px solid #eee;font-weight:500;
                         color:#555;width:35%;vertical-align:top">{k}</td>
              <td style="padding:8px 12px;border-bottom:1px solid #eee;
                         font-family:monospace;font-size:13px">{v}</td>
           </tr>"""
        for k, v in payload.items()
    )
    return f"""
    <html><body style="font-family:sans-serif;max-width:620px;margin:0 auto;color:#111">
      <h2 style="font-size:17px;font-weight:600;margin-bottom:4px">{subject}</h2>
      <p style="font-size:12px;color:#999;margin-top:0">
        Received {datetime.now().strftime('%A %d %B %Y · %H:%M:%S')}
      </p>
      <table style="width:100%;border-collapse:collapse;font-size:14px;
                    border:1px solid #eee;border-radius:6px;overflow:hidden">
        <thead>
          <tr style="background:#f5f5f5">
            <th style="padding:9px 12px;text-align:left;font-weight:500">Field</th>
            <th style="padding:9px 12px;text-align:left;font-weight:500">Value</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
      <p style="font-size:11px;color:#bbb;margin-top:18px">
        Sent by Flask Webhook · /webhook endpoint
      </p>
    </body></html>"""


def send_alert(
    subject: str,
    payload: dict,
    sender: str,
    password: str,
    recipient: str,
) -> bool:
    """Send an HTML alert email for an incoming webhook payload."""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    plain = "\n".join(f"{k}: {v}" for k, v in payload.items())
    msg.attach(MIMEText(plain, "plain"))
    msg.attach(MIMEText(_build_html(subject, payload), "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, recipient, msg.as_string())
        return True
    except smtplib.SMTPAuthenticationError:
        print("  [notifier] Gmail auth failed — check EMAIL_PASSWORD in .env")
        return False
    except Exception as e:
        print(f"  [notifier] Email error: {e}")
        return False
