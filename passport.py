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
EMAIL_TO = ["eam@mea.gov.in"
]
EMAIL_CC = ["passport.admin@passportindia.gov.in","diream@mea.gov.in","jseamo@mea.gov.in","useamo@mea.gov.in","useam@mea.gov.in","rpo.dehradun@mea.gov.in","jscpo@mea.gov.in","passport.pg@mea.gov.in"
]

subject = "Urgently Request for Immediate Look The Matter MEAPD/E/2025/0002828 || New File No - DD7070915890025"

body = """\

To,
Dr. S. Jaishankar
Hon’ble Minister of External Affairs
Ministry of External Affairs
South Block, New Delhi – 110011
India

Subject: Urgent Humble Request/Complaint-MEAPD/E/2025/0002828 for Removal of Police Verification Hold & Immediate Release of Passport File No-DD7070915890025.

Dear Hon’ble Minister,

My name is Rohit Rawat, and I humbly write to seek your kind intervention in a matter of urgency concerning the reissue of my passport. My application is currently on hold due to police verification, despite being a renewal request with no changes to personal details or address.

Application Details:
• File Number: DD7070915890025
• Old Passport Number: N7638881
• Submission Date: 17th April 2025
• Passport Seva Kendra: POPSK Srinagar, Pauri Garhwal, Uttarakhand
• Type of Application: Reissue – Normal
• Current Status: On Hold – Subject to Police Verification
• Current Passport Validity: Until May 2026

I wish to respectfully inform you that I have been admitted to the University of East London to pursue my Master of Science in Artificial Intelligence, starting in the upcoming academic session. As per UK visa requirements, I must submit a passport with at least two years of validity in order to be granted a Tier-4 (Student) Visa valid for the duration of the course.

My current passport, valid only for one more year, does not meet this eligibility, and therefore, I have applied for a reissue solely to extend its validity, without any changes to my information or credentials.

All my documents have been verified, and no additional documents are pending. Therefore, I kindly request you to:
1. Remove the police verification hold from my application.
2. Issue instructions to the Regional Passport Office, Dehradun (under Mr. Vijay Shankar Pandey) rpo.dehradun@mea.gov.in, to immediately release my reissued passport.
3. Help expedite the process so that I can meet my visa timeline and academic commitments abroad.

Your support in this matter would enable me to pursue my educational goals and represent India at an international level. I would be deeply grateful for your guidance and prompt intervention.

Thank you for your consideration.

Sincerely,

"""

# List of files to attach
PDF_FILES = ["Acknowledgement_Slip.pdf","old passport back side.png","old passport front side.png"]

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