**Automated Investment News Notifier**

This Python script serves as an automated tool for keeping you updated on the latest investment news. The script monitors a specified RSS feed, in this case, focusing on financial news from the BBC Turkish website, and sends email notifications whenever new entries are detected. The Gmail SMTP server is utilized for seamless email delivery.

**Key Features:**
- **RSS Feed Integration:** The script leverages the `feedparser` library to efficiently parse the specified RSS feed (e.g., 'https://www.bbc.com/turkce/ekonomi/index.xml') for the latest investment-related articles.

- **Email Notifications:** Email alerts are sent using the Gmail SMTP server, providing a convenient way to receive timely updates. The script uses the `smtplib` library for email handling and `email.mime.text` for constructing email content.

- **Continuous Monitoring:** The script runs indefinitely, regularly checking for new entries in the RSS feed. The default interval is set to 60 seconds (adjustable), ensuring frequent updates without the need for manual intervention.

**Usage:**
1. Clone the repository.
2. Set the RSS feed URL (`rss_url`) and your Gmail account credentials (`gmail_username` and `gmail_password`).
3. Customize the email subject (`subject`) and recipient address (`to_email`) as needed.
4. Run the script and stay informed about the latest investment news directly in your inbox.

**Possible Future Features:**
- **Multiple RSS Feed Support:** Extend the script to monitor multiple RSS feeds simultaneously, allowing users to track news from various sources.

- **User Configuration:** Implement a configuration file or user interface for easy customization of script parameters such as feed URL, email settings, and update frequency.

- **Database Integration:** Store and manage a history of previously sent articles in a database for reference and analysis.

- **Advanced Email Formatting:** Enhance email content with HTML formatting, embedded links, or additional metadata for a richer user experience.

- **Logging and Error Handling:** Implement a robust logging system to capture errors, successful operations, and relevant information for troubleshooting.

Feel free to contribute, customize, or suggest additional features to make this Automated Investment News Notifier even more powerful and user-friendly!
