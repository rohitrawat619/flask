import smtplib
import schedule
import time

# Email credentials
EMAIL_SENDER = "rohitrawat676@gmail.com"
EMAIL_PASSWORD = "zkgdqjvyngyihsge"  # Use App Password for security
EMAIL_RECEIVERS = [
    "migrationsverket@migrationsverket.se",
    "culture.stockholm@mea.gov.in",
    "hoc.stockholm@mea.gov.in"
    "stockholm-arbetstillstandsenhet3@migrationsverket.se",
    "arbetstillstandsenhet3@migrationsverket.se",
    "rohitrawat8126844298@gmail.com",
    "sandra.nunez@migrationsverket.se"
    ]

def send_email():
    subject = "Request Regarding Refund My Resident Permit Visa fees || Control no 62151395"
    body = """\
        Dear Sandra Nunez,
        Be assured of the withdrawal of my application in a full refund of visa fees condition only that is Euro 210. 
        Kindly, withdraw my application with control no 62151395 & refund visa fees to my bank account ICIC A/C - 016401026756 & IFSC Code - ICIC0000164.
        Best regards,
        """

    email_message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, email_message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# send_email()

schedule.every(1).minutes.do(send_email)

print("Scheduler started...")

# 🔁 Keep the schedule running
while True:
    schedule.run_pending()
    time.sleep(60)