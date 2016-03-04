'''PYTHON MAILER
This code is intended to send 
messages with attachments 
using the Citadel email program
for Raspberry Pi
________________________________
How to get this code working
________________________________
INSTALL CITADEL SUITE

-http://tinkernut.com/TTlC5

'''

#create a variable set to the location of the "sendmail" program
SENDMAIL = "/usr/sbin/sendmail"

#import the Text,Image and Multipart modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#create variables for the "to" and "from" email addresses
TO = ["email_address_of_receiver"]
FROM = "email_address_of_sender"

#asemble the message as "MIMEMultipart" mixed
msg = MIMEMultipart('mixed')
msg['Subject'] = 'Python test mail'
msg['From'] = FROM
msg['To'] = ', '.join(TO)
body = MIMEText('I hope you recieve this!', 'plain')
msg.attach(body)

#open up an image file and attach it to the message
img_data = open('png_file.png', 'rb')
image = MIMEImage(img_data.read())
img_data.close()
msg.attach(image)

#import the os library and use it to open up sendmail, write the message, and close it
import os
p = os.popen("%s -t -i" % SENDMAIL, "w")
p.write(msg.as_string())
status = p.close()
