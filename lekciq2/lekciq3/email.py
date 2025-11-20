import smtplib
from email.message import EmailMessage

sender_email = ""
receiver_email = ""
password = ""

smtp_server = "smtp.gmail.com"
port = 587  

msg = EmailMessage()
msg['Subject'] = "zadachata"
msg['From'] = ""
msg['To'] = ""
msg.set_content("Zadachata.")

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")