import smtplib
import schedule
import time

# Email credentials
EMAIL_SENDER = "rohitrawat676@gmail.com"
EMAIL_PASSWORD = "zkgdqjvyngyihsge"  # Use App Password for security
EMAIL_RECEIVERS = [
    "migrationsverket@migrationsverket.se",
    "culture.stockholm@mea.gov.in",
    "hoc.stockholm@mea.gov.in",
    "masoud.moghbel@migrationsverket.se",
    "stockholm-arbetstillstandsenhet3@migrationsverket.se",
    "arbetstillstandsenhet3@migrationsverket.se",
    "rohitrawat8126844298@gmail.com",
    "sandra.nunez@migrationsverket.se"
    ]


subject = "Urgent Follow-Up: Refund Request for MyControl Number 62151395 || Delay In Refund Process"
body = """\
Dear Swedish Migration Agency,

I hope this email finds you well. I am writing to follow up on my refund request for MyControl Number 62151395 which has not yet been processed despite my previous communications.You already have confirmed the refund process on date  24/Mar/2025 as per email officially discussion by @masoud.moghbel@migrationsverket.se . However, I have yet to receive the refund or any further updates. Below are the details of my payment: .

• Full Name: Rohit Rawat  
• MyControl Number: 62151395  
• Account Number: 104601026756  
• Swift Code: ICICINBBNRI  
• IFSC Code: ICIC0000164  

@migrationsverket@migrationsverket.se, @masoud.moghbel@migrationsverket.se & @sandra.nunez@migrationsverket.se Look at the matter urgently, please.

I kindly request you to expedite the process and provide me with a clear timeline for when I can expect the refund. 

If there are any additional formalities required from my side, please let me know at the earliest.I appreciate your immediate attention to this matter and look forward to your response.
        
Best regards,
"""

# Ensure all text is properly encoded
body = body.replace("\xa0", " ")  # Replace non-breaking spaces

def send_email():
    email_message = f"Subject: {subject}\nMIME-Version: 1.0\nContent-Type: text/plain; charset=utf-8\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, email_message.encode('utf-8'))
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Schedule the email every minute
schedule.every(1).minutes.do(send_email)

print("Scheduler started...")

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(60)
