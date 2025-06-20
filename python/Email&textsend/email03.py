import imapclient , pyzmail
# Email providers and their IMAp servers 
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# logging in to IMAP server
password = input("Password : ")
imapObj.login('ibrahimadebanjo283@gmail.com', str(password))

imapObj.select_folder('INBOX', readonly=True)
# Performing a Search
UIDs = imapObj.search(['SINCE 05-Jul-2014'])
# UIDs are unique interger values returned that represent the emails
print(UIDs)
# Use fetch() method to obtain the email content
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
message.get_subject()
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('cc'))
print(message.get_addresses('bcc'))
print(message.text_part != None)
print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part != None)
print(message.html_part.get_payload().decode(message.html_part.charset))
# Deleting emails
# This marks the email with delete flag 
imapObj.delete_messages(UIDs)
# This permanently delete the email
imapObj.expunge()

# Disconnecting from the IMAP Server

imapObj.logout()