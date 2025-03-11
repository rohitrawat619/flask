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

send_email()

# Schedule the email every morning at 8 AM
schedule.every().day.at("01:00").do(send_email)  # 1 AM
schedule.every().day.at("02:00").do(send_email)  # 2 PM
schedule.every().day.at("03:00").do(send_email)  # 3 AM
schedule.every().day.at("04:00").do(send_email)  # 4 PM
schedule.every().day.at("05:00").do(send_email)  # 5 PM
schedule.every().day.at("06:00").do(send_email)  # 6 AM
schedule.every().day.at("07:00").do(send_email)  # 7 PM
schedule.every().day.at("08:00").do(send_email)  # 8 AM
schedule.every().day.at("09:00").do(send_email)  # 9 PM
schedule.every().day.at("10:00").do(send_email)  # 10 AM
schedule.every().day.at("11:00").do(send_email)  # 11 PM
schedule.every().day.at("12:00").do(send_email)  # 12 PM
schedule.every().day.at("13:00").do(send_email)  # 13 AM
schedule.every().day.at("14:00").do(send_email)  # 14 PM
schedule.every().day.at("15:00").do(send_email)  # 15 AM
schedule.every().day.at("16:00").do(send_email)  # 16 PM
schedule.every().day.at("17:00").do(send_email)  # 17 AM
schedule.every().day.at("18:00").do(send_email)  # 18 PM
schedule.every().day.at("19:00").do(send_email)  # 19 PM
schedule.every().day.at("20:00").do(send_email)  # 20 AM
schedule.every().day.at("21:00").do(send_email)  # 21 PM
schedule.every().day.at("22:00").do(send_email)  # 22 PM
schedule.every().day.at("23:00").do(send_email)  # 23 PM
schedule.every().day.at("00:00").do(send_email)  # 23 PM

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute



