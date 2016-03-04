'''PYTHON GMAILER
This code is intended to send 
messages with attachments 
through gmail using python.
________________________________
How to get this code working
________________________________
INSTALL KEYRING
-pip install keyring

INSTALL KEYRING ALT
wget https://pypi.python.org/packages/source/k/keyrings.alt/keyrings.alt-1.1.tar.gz
tar -zxvf keyrings.alt-1.1.tar.gz
cd keyrings.alt-1.1
python setpy.py install

ENABLE GMAIL TO ALLOW THIRD-PARTY PROGRAMS
- without dual authentication: http://www.google.com/settings/security/lesssecureapps
- without dual authentication: https://security.google.com/settings/security/apppasswords

'''
import smtplib
import keyring

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

gmail_acct = "your_gmail_account"
app_spec_pwd = keyring.get_password("credentials", "gmail")

TO = ["email_address_of_receiver"]
FROM = "email_address_of_sender"

msg = MIMEMultipart('mixed')
msg['Subject'] = 'Python test mail'
msg['From'] = FROM
msg['To'] = ', '.join(TO)
body = MIMEText('I hope you recieve this!', 'plain')
msg.attach(body)

img_data = open('png_file.png', 'rb')
image = MIMEImage(img_data.read())
img_data.close()
msg.attach(image)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo
server.login(gmail_acct, app_spec_pwd)
server.sendmail(FROM, TO, msg.as_string())
server.close()
