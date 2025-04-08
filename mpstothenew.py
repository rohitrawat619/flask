import smtplib
import schedule
import time
from email.message import EmailMessage

# Email credentials
EMAIL_SENDER = "rohitrawat676@gmail.com"
EMAIL_PASSWORD = "zkgdqjvyngyihsge"  # Use App Password for security

# Specify TO and CC separately
EMAIL_TO = [
            "abhilash.sharma@highwirepress.com",
            "preetam.panda@mpslimited.com",
            "umakant.vajpayee@mpslimited.com",
            "gaurav.chouhan@mpslimited.com",
            "clal@mpslimited.com",
            "gunjan.naik@mpslimited.com",
            "sneha.yadav@highwirepress.com",
            "kishan.kumar@highwirepress.com",
            "aditya.singh@highwirepress.com",
            "rsatija@highwirepress.com",
            "nsingh@highwirepress.com",
            "vraterwal@highwirepress.com",
            "vijay.sharma@mpslimited.com",
            "prashant.nigam@highwirepress.com",
            "Neeraj.pan28@gmail.com"
]

EMAIL_CC = [
     "sudha.n@mpslimited.com",
     "yash.bichchal@mpslimited.com",
     "Sangeeta.mandal@mpslimited.com",
     "aditi.gupta@mpslimited.com",
     "neeraj.rana@mpslimited.com",
     "taruna.singh@mpslimited.com",
     "rsatija@highwirepress.com",
     "nsingh@highwirepress.com",
     "pooja.bhatt@mpslimited.com",
     "tahaseen.s@mpslimited.com",
     "abhishek.sharma@mpslimited.com",
     "shaily.virmani@mpslimitd.com",
     "aarti.yadav@mpslimited.com",
     "awadh.rajput@mpslimited.com",
     "hemanti.sarkar@mpslimited.com",
     "mohit.singh@mpslimited.com",
     "purushotta.d@mpslimited.com",
     "raman.shapra@mpslimited.com",
     "Prarthana.agarwal@mpslimited.com",
     "rahul.arora@mpslimited.com",
     "geetika.hans@mpslimited.com",
     "secretarial@mpslimited.com",
     "Prarthana.agarwal@mpslimited.com"
     ]

subject = "Exciting Opportunity at TO THE NEW Pvt. Ltd. for Drupal Developers || Minimum Package 10+ LPA"
body = """\
Dear MPS Drupal Team,

I hope this message finds you all in great health and high spirits.

I’m thrilled to share a fantastic opportunity with all of you. My previous Singapore-based company, TO THE NEW Pvt. Ltd., is currently expanding its Drupal development team and offering competitive packages ranging from ₹15 to ₹20 LPA for experienced professionals.

As a former team member, I can confidently say that this organization provides a thriving environment for Drupal developers to grow, innovate, and lead. Their commitment to technology and talent is exceptional, and they are actively looking for skilled developers who can contribute meaningfully to their projects.

I attached naukri.com Link with a screenshot to grab the opportunity.

https://www.naukri.com/job-listings-drupal-developer-to-the-new-noida-3-to-7-years-270325017220

Why Consider TO THE NEW Pvt. Ltd.?

Unmatched Benefits & Culture:

🏫 Education & Certification Reimbursement
🎉 Regular Client Parties & Events
🧑‍💻 Hybrid Work Culture
✈️ Offsite Trips with Combo Off Days
💸 Minimum 35% Yearly Salary Increment

This is an incredible chance to elevate your career in a forward-thinking company that values both professional and personal growth.

Let’s Grab the Opportunity!
If you’re interested or would like to know more, feel free to reach out. I’d be happy to make a personal referral and help you take the first step toward this exciting new chapter.

Warm regards,

Rohit Rawat

Former Drupal Developer, TO THE NEW Pvt. Ltd.
"""

attachments = ["mps.png"]

# Attachments

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