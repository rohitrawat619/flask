import smtplib
import schedule
import time
from email.message import EmailMessage

# Email credentials
EMAIL_SENDER = "rohitrawat676@gmail.com"
EMAIL_PASSWORD = "zkgdqjvyngyihsge"  # App Password

# Primary recipients (To)
EMAIL_TO = [
    "masoud.moghbel@migrationsverket.se",
    "migrationsverket@migrationsverket.se",
    "pernilla.eriksson@migrationsverket.se",
    "sandra.nunez@migrationsverket.se"
]

# CC recipients
EMAIL_CC = [
]

subject = "Request for Clarification and Refund of My SEK 132 Remaining Amount from Visa Application Fee Control No-62151395 || Ref: 2025040100281601 || ICICI= E029747594"

body = """\
Dear Sir/Madam,
Swedish Migration Agency

I hope this message finds you well.

I am writing to formally raise a concern regarding the recent refund I received related to my visa application fee. 
While the original payment I made was 2,200 SEK on 2/July/2024, I only received an amount equivalent to approximately 
2069 SEK which is 132 SEK less than the full amount that is 2,200 SEK, which is significantly unexpected.

At the time of payment, the full amount of 2,200 SEK was successfully debited from my account. 
I therefore request a clarification as to why the refunded amount does not reflect the full value paid. 
I respectfully ask for the remaining balance to be returned to me as soon as possible.

Kindly review this matter urgently and provide a breakdown of the refund calculation, if applicable. 
I believe this may have been an oversight or a technical issue, and I would appreciate your swift assistance in resolving it.

I have attached the payment receipt and refund detail as evidence of the payment made and the refund received. 
Please let me know if you require any further information or documentation from my side to expedite this process.

ICICI Bank A/C: 016401026756  
SWIFT Code: ICICINBBNRI  
IFSC Code: ICIC0000164

Warm regards, 
"""

# Attachments
attachments = ["CreditCardStatement.pdf", "Remittance_Evidence.png"]

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