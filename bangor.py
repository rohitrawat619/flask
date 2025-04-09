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

subject = "Request for £10,000 Vice-Chancellor Scholarship || Amendment offer Letter || Student Number- 500762104"

body = """\

Dear Sir/Madam,
I hope this message finds you well.

My name is Rohit Rawat, and I am writing to express my keen interest in the Vice-Chancellor’s Scholarship offered by your esteemed university. I am highly motivated to pursue my academic goals at Bangalore University, Wales, and this scholarship would significantly support my educational journey.

I humbly request you to kindly consider my application for the £10,000 Vice-Chancellor’s Scholarship. I am confident that with this support, I will be able to focus wholeheartedly on my studies and contribute positively to the university community.

Please let me know if there are any documents or additional information required from my end to process this request.

Please let me know if there are any additional documents or formalities required from my side to initiate this amendment.

https://www.bangor.ac.uk/international/scholarship

Kindly, Update my offer letter with a new tuition fee excluding scholarship which I calculated as  £ 15,000.

I attached the offer letter below for your reference.

I am looking forward to your prompt response regarding this matter. I understand that you may be busy, but I would greatly appreciate any assistance you can provide.

I sincerely appreciate your assistance and look forward to your positive response.

Warm regards,

Student Number-500762104

Thank you for your time and consideration.

Warm regards,

"""

# List of files to attach
PDF_FILES = ["Rawat-Rohit-500762104-MSC_ADS-1.pdf"]

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