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
EMAIL_TO = ["rpo.dehradun@mea.gov.in","jscpo@mea.gov.in","passport.pg@mea.gov.in"
]
EMAIL_CC = ["passport.admin@passportindia.gov.in"
]

subject = "Urgent Request for Immediate Release of Reissue Passport Under Renewal Category Without Any Changes || New File No - DD7070915890025"

body = """\

To,

Mr. Vijay Shankar Pandey
Regional Passport Officer
12, New Road, Aroma Hotel,
Dehradun, Uttarakhand-248001

Dear Mr. Pandey,

I am writing to ask for the immediate release of my new passport, which was submitted under the renewal category without any changes. Please note that no changes have been requested in the existing passport details.

The details of my application are as follows:

Old Passport Number: N7638881
New File Number: DD7070915890025

Given that the renewal process does not involve any updates or changes to the document, I humbly request that you facilitate the release of my passport within 3 working days, please, so that I can take the London University interview with a new passport number, which will be future use for applying for a visa.

Your prompt attention and acknowledgement of this request will be highly appreciated, as I am in urgent need of my passport.

Thank you for your support and cooperation.

Sincerely,

"""

# List of files to attach
PDF_FILES = ["Acknowledgement_Slip.pdf","old passport back side.png","old passport back side.png"]

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