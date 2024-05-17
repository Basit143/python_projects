import smtplib
from email.mime.text import MIMEText

# Replace with your email credentials
sender_email = "your_email@example.com"
sender_password = "your_password"

# Replace with recipient email address
recipient_email = "recipient_email@example.com"

# Create email message
message = MIMEText("This is a test email.")
message["Subject"] = "Test Email from Python"
message["From"] = sender_email
message["To"] = recipient_email

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Email sent successfully!")