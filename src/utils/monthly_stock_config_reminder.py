# 0 9 1 * * /usr/bin/python3 /path/to/monthly_stock_config_reminder.py

import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def send_reminder():
    msg = MIMEText(f"""
Monthly Reminder: Update Stock Name & Ticker Configs

Date: {datetime.now().strftime("%Y-%m-%d")}

Tasks:
 - Download latest Nifty 50 list.
 - Regenerate Yahoo tickers (.NS).
 - Validate ticker changes.
 - Update your config and redeploy.

""")

    msg["Subject"] = "Monthly Reminder: Update Stock Configs"
    msg["From"] = "noreply@yourcompany.com"
    msg["To"] = "team@yourcompany.com"

    s = smtplib.SMTP("smtp.yourcompany.com")
    s.sendmail(msg["From"], [msg["To"]], msg.as_string())
    s.quit()

if __name__ == "__main__":
    send_reminder()
