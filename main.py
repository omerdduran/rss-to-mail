import feedparser
import smtplib
from email.mime.text import MIMEText
import time
from datetime import datetime, timezone  # Import timezone

# RSS Feed URL
rss_url = 'https://www.bbc.com/turkce/ekonomi/index.xml'

# Gmail account credentials
gmail_username = 'your_email@gmail.com'
gmail_password = 'your_gmail_password'

# Email settings
to_email = 'trigger@applet.ifttt.com'
subject = 'Investment News'
from_email = gmail_username

def check_for_new_entries(last_entry_published):
    # Fetch data from the RSS feed
    feed = feedparser.parse(rss_url)

    # Get the publication date of the latest entry
    latest_entry = feed.entries[0]
    latest_entry_published = datetime.strptime(latest_entry.published, "%Y-%m-%dT%H:%M:%S%z")

    # Associate last_entry_published with UTC
    last_entry_published = last_entry_published.replace(tzinfo=timezone.utc)

    # If the latest entry is different from the previously checked entry
    if latest_entry_published > last_entry_published:
        # There is a new entry, send an email
        summary = latest_entry.summary
        email_body = f"🔴 {summary}"
        send_email(email_body)

        # Update the publication date of the last entry
        return latest_entry_published

    # No new entry, continue with the same date
    return last_entry_published

def send_email(body):
    # Create email content
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Send email via Gmail
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(gmail_username, gmail_password)
        server.sendmail(from_email, to_email, msg.as_string())

if __name__ == "__main__":
    last_entry_published = datetime.min.replace(tzinfo=None)  # Start with the smallest date
    while True:
        last_entry_published = check_for_new_entries(last_entry_published)
        time.sleep(60)  # Check every minute by waiting for 60 seconds
