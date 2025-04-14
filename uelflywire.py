import smtplib
import schedule
import time
from email.message import EmailMessage

# Email credentials
EMAIL_SENDER = "rohitrawat676@gmail.com"
EMAIL_PASSWORD = "zkgdqjvyngyihsge"  # App Password

# Primary recipients (To)
EMAIL_TO = [
    "support@flywire.com",
    "flywiretcs@in.luluforex.com"
]

# CC recipients
EMAIL_CC = [
    "flywiredocuments@in.luluforex.com"
]

subject = "Urgent Request to Forward Payment to the University of East London || Payment ID - UEI679419784 || Beneficiary A/C-LULU150504599"

body = """\
Dear Flywire and Lulu Virtual Account Support Team,

I hope this message finds you well.

I am writing to request your immediate assistance in forwarding my recent transaction to the University of East London. This payment is time-sensitive, and it must reach the university without further delay to avoid any negative impact on my enrollment process.

Please treat this matter as urgent and ensure the payment is processed and forwarded to the designated university account as soon as possible.

Your prompt action and confirmation would be greatly appreciated & I attached evidence below as a screenshot.

Kindly, proceed fast with my payment as soon as possible

Payment ID - UEI679419784

Best regards,
"""

# Attachments
attachments = ["UEL.pdf", "LULU150504599.pdf","flywire.png", "uel.png"]

def send_email():
    msg = EmailMessage()
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(EMAIL_TO)
    msg["Cc"] = ", ".join(EMAIL_CC)
    msg["Subject"] = subject
    msg.set_content(body)

    for file_path in attachments:
        try:
            with open(file_path, "rb") as f:
                file_data = f.read()
                file_name = f.name
                msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
        except Exception as e:
            print(f"Could not attach file {file_path}: {e}")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully with attachments!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Schedule email every 1 minute
schedule.every(1).minutes.do(send_email)

print("Scheduler started... sending email every 1 minute")

while True:
    schedule.run_pending()
    time.sleep(60)