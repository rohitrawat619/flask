import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
EMAIL_SENDER = "rohitrawat676@gmail.com"
EMAIL_PASSWORD = "zkgdqjvyngyihsge"  # Use App Password for security

# Specify TO and CC separately
EMAIL_TO = ["rahul.arora@mpslimited.com","geetika.hans@mpslimited.com","secretarial@mpslimited.com","Prarthana.agarwal@mpslimited.com"]
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

]

subject = "Request Regarding for Salary Revision to 10 form 8 LPA || Resignation Letter - MPS Limited L22122TN1970PLC005795"
body = """\
Dear Rahul & Geetika,

I am forwarding the previous email I sent to the lower division officer, Request Regarding Salary Revision to 10 LPA from 8 LPA || About Resignation Letter. 

I wanted to bring this to your attention for further expectations/hope and support.

Please review the conversation below for full details.

Best regards, 


---------- Forwarded message ---------
From: Rohit Rawat <rohitrawat676@gmail.com>
Date: Wed, Apr 2, 2025 at 11:35 PM
Subject: Request Regarding for Salary Revision to 10 LPA form 8 LPA || About Resignation Letter
To: <nsingh@highwirepress.com>
Cc: Sudha N <sudha.n@mpslimited.com>, Rahul satija <rsatija@highwirepress.com>, <neeraj.rana@mpslimited.com>, Yash Bichchal <yash.bichchal@mpslimited.com>

Respected Naresh Kumar,

It is with great disappointment that I must write this request. I am formally requesting a salary revision from 8 LPA to 10 LPA, as discussed before or after my MPS Ltd interview process before my interview, Sudha N sudha.n@mpslimited.com from the HR team MPS Bangalore informed me that the budget for the Drupal Developer role was around 10 to 12 LPA, which was a key reason for my participation in the interview process. However, my offer letter mentioned 8 LPA after a mutual discussion with disappointment. I had already communicated my expected salary to Yash Bichchal yash.bichchal@mpslimited.com, but it seems my expectations were not fully considered.

Given my contributions and responsibilities in this role, I believe a salary adjustment to 10 LPA is reasonable and aligns with the discussed budget before & after Interview. I feel very demotivated by my current CTC.

I humbly request you to review my request and give a decision in between April 3 to April 6. If the amendment is not possible by EOD April 6, I may have to consider discontinuing the job with MPS Limited unfortunately.

I appreciate your time and consideration and look forward to your response.

Thanks & Regards

Emp I.D - MAC012861
"""

def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = ", ".join(EMAIL_TO)
        msg['Cc'] = ", ".join(EMAIL_CC)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_TO + EMAIL_CC, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the email to be sent every 60 seconds
schedule.every(60).seconds.do(send_email)

print("Email scheduling started. Press Ctrl+C to stop.")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)