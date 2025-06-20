import smtplib

sender = "ibrahimadebanjo283@gmail.com"
reciever = "ibrahimadebanjo2443@gmail.com"
subject = "I am a software developer and a AI/ML Engineer"
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(smtpObj.ehlo())
# logging in to SMTP server
password = input("password :")
smtpObj.login("ibrahimadebanjo283@gmail.com", str(password))
# sending an Email
smtpObj.sendmail(sender, reciever, subject)
{}
# disconnecting from the server
smtpObj.quit()

