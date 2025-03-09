# import smtplib
# import schedule
# import time

# # Email credentials
# EMAIL_SENDER = "rohitrawat676@gmail.com"
# EMAIL_PASSWORD = "Sbi@2089676@"  # Use App Password for security
# EMAIL_RECEIVER = "rohitrawat8126844298@gmail.com"

# def send_email():
#     subject = "Good Morning!"
#     body = "Hey buddy, have a great day! 😊"

#     email_message = f"Subject: {subject}\n\n{body}"

#     try:
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()
#             server.login(EMAIL_SENDER, EMAIL_PASSWORD)
#             server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message)
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Error: {e}")

# send_email()


# # Schedule the email every morning at 8 AM
# schedule.every().day.at("08:00").do(send_email)

# print("Scheduler started...")

# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Check every minute


import smtplib
import schedule
import time

# Email credentials
EMAIL_SENDER = "rohitrawat676@gmail.com"
EMAIL_PASSWORD = "Sbi@2089676@"  # Use App Password for security
EMAIL_RECEIVER = "rohitrawat8126844298@gmail.com"

def send_email():
    subject = "Good Morning!"
    body = "Hey buddy, have a great day! 😊"

    email_message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Send email instantly on script start
send_email()

# Schedule the email every morning at 8 AM
schedule.every().day.at("08:00").do(send_email)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute