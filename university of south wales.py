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
EMAIL_TO = [
    "international@bangor.ac.uk,"
    "postgraduate@bangor.ac.uk",
    "internationaladmissions@bangor.ac.uk",
    "internationalsupport@bangor.ac.uk"
]
EMAIL_CC = [
    "cahb@bangor.ac.uk"
]

subject = "Request for Unconditional Offer Letter – Submitted Recommendation Letter from Byanric Systems Employer || Student Number- 23106423"

body = """\

Dear Joanna Scaplehorn,

University of South Wales

I hope this message finds you well.

I am writing to kindly request the issuance of my unconditional offer letter for the M.sc Data Science program. I have recently submitted a letter of recommendation from my previous employer, Bynaric Systems Pvt Ltd, as per the documentation requirements.

Please confirm if the recommendation letter has been received and whether there are any additional documents or steps needed to proceed with the issuance of the unconditional offer.

I am very excited about the opportunity to study at the University of South Wales and am looking forward to joining your esteemed institution.

I understand that you may be busy, but I would be grateful if you could prioritize this request. If there are any issues or further information needed, please do not hesitate to reach out to me.

Thank you for your support and assistance.

Kind regards,
Rohit Rawat
Student Number-23106423

Thank you for your time and consideration.
"""

# List of files to attach
PDF_FILES = ["Bynaric Systems Experience-Letter-Rohit Rawat.pdf","Conditional Offer Letter (18).pdf"]

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