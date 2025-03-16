import smtplib
import schedule
import time

# Email credentials
EMAIL_SENDER = "rohitrawat676@gmail.com"
EMAIL_PASSWORD = "zkgdqjvyngyihsge"  # Use App Password for security
EMAIL_RECEIVERS = [
    "support@duolingo.com",
    "press@duolingo.com",
    "englishtest@duolingo.com",
    "rohitrawat8126844298@gmail.com"
    ]

def send_email():
    subject = "Request for Refund of Duolingo English Test Fee || Payment Method by VISA - XXXX-XXXX-XXXX-9004"
    body = """\
        I hope this message finds you well. I am writing to request a refund for the Duolingo English Test I recently purchased on 2/Mar/2025
        I have not started or attempted the test, and the purchase was made within the 21-day refund window. Therefore, I kindly request that the test fee be refunded to my original payment method.
        Here are my details:
        Name: Rohit Rawat
        Email associated with my Duolingo account: rohitrawat676@gmail.com
        Date of Purchase: Mar 02, 2025
        I would appreciate it if you could process the refund at your earliest convenience. Please let me know if any additional information is needed from my side.
        Thank you for your assistance. Regards,
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