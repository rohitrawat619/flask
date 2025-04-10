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
]
EMAIL_CC = [
    "p.bawa@uel.ac.uk",
    "k.gandhi@uel.ac.uk ",
    "S.Choudhury3@uel.ac.uk ",
    "N.bhasson@uel.ac.uk ",
    "g.krishnamurthy@uel.ac.uk",
    "k.walunj@uel.ac.uk ",
]

subject = "Request for Immediate Release of Unconditional Offer Letter and Confirmation of Admission Reservation || May Intake 2025"

body = """\
Dear Admissions Team,

University of East London

I hope this message finds you well.

I am writing to kindly request the immediate release of my Unconditional Offer Letter for course MSc Artificial Intelligence , as it is urgently required by my bank to process the financing of aneducation loan for my studies from the State Bank of India.

Additionally, I would be grateful if you could please confirm and ensure that my admission/reservation at the University of East London is secure, as I am fully committed to joining the program.

Please let me know if any further documentation or actions are needed from my side to expedite this request. Your prompt assistance in this matter would be highly appreciated.

I attached a portal screenshot for your reference below.

Thank you very much for your support and understanding.

Warm regards,.
Rohit Rawat
"""

# List of files to attach
PDF_FILES = ["east_london.png"]

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