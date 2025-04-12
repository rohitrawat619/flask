import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email credentials
EMAIL_SENDER = "rohitrawat676@gmail.com"
EMAIL_PASSWORD = "zkgdqjvyngyihsge"  # Use App Password for security

# Specify TO and CC separately
EMAIL_TO = ["rpo.dehradun@mea.gov.in"
]
EMAIL_CC = ["international@bangor.ac.uk"
]

subject = "Request for Early Renewal of Passport for Higher Education Abroad || Passport N7638881"

body = """\

Respected Sir/Madam,

I hope this message finds you well.

I am writing to request your kind consideration for the early renewal of my passport. My current passport is valid until  24 May 2026, which is a little over 12 months from today. As per standard procedure, I understand that passport renewal is normally permitted within 12 months of expiry.

However, I am planning to pursue my higher studies in the United Kingdom for approximately 1.5 years, and my university admission and visa process are time-sensitive. To meet the UKVI requirements and visa application timeline, I must possess a passport with validity well beyond the duration of my stay.

I kindly request you to allow the early reissue of my passport so that I can proceed with my visa formalities in time. I am prepared to provide my university offer letter and any other supporting documents required to justify this request.

I sincerely hope for your understanding and support in this matter. Your assistance will help me take the next big step in my academic and professional journey.

Thank you for your time and consideration.

Warm regards,

"""

# List of files to attach
PDF_FILES = [""]

def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = ", ".join(EMAIL_TO)
        msg['Cc'] = ", ".join(EMAIL_CC)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Attach multiple files
        for file_path in PDF_FILES:
            with open(file_path, "rb") as attachment:
                part = MIMEApplication(attachment.read(), Name=file_path)
                part['Content-Disposition'] = f'attachment; filename="{file_path}"'
                msg.attach(part)

        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_TO + EMAIL_CC, msg.as_string())

        print("✅ Email sent successfully with attachments!")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Schedule the email to run every 60 seconds
schedule.every(60).seconds.do(send_email)

print("📧 Email scheduler started. Sending every 60 seconds...")

# Keep running
while True:
    schedule.run_pending()
    time.sleep(1)