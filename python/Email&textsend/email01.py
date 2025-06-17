import smtplib
from email.mime.text import MIMEText

# Define eamil Parameters
senderMail = "ibrahimadebanjo283@gmail.com"
receiverEmail = "zulupapa@gmail.com"
subject = "Text Email"
body = "Hello bro, This text is sent using python"

# Create email message
msg = MIMEText(body)
msg[subject] = subject
msg["From"] = senderMail
msg["To"] = receiverEmail

#  send the mail using SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderMail, "Your password")
server.sendmail(senderMail,  receiverEmail, msg.as_string())
server.quit()
# NB: USE smtp.gmail.com with port 587(TLS) or 465(SSL) 
# check other 